"""
Python Script to simulate Three-Address Code (TAC)
Thomas Mason Nelson <nelsontm@umich.edu>
April 2022, for eecs483 @ umich
"""

import argparse
import os
import sys

def get_argparser() -> argparse.ArgumentParser:
    """Create an argparser for the test verifier"""
    
    parser = argparse.ArgumentParser(
            description="Parse arguments for TAC simulation")

    parser.add_argument("file",
            type=str, 
            help="Which TAC file to simulate")

    parser.add_argument("-s", "--stats",
            const=True, default=False, nargs='?', required=False,
            help="Print instruction statistics.")

    return parser

def read_lines(file_name: str) -> [str]:
    """
    Reads in the lines from a file
    :param file_name:   The name of the file
    :return:            The lines from the file
    This eliminates the need to use a with statement for each open file
    """
    with open(file_name, "r") as read_file:
        return read_file.readlines()

parser = get_argparser()
args = parser.parse_args()

# Ensure test file exists
if not os.path.isfile(args.file):
    print("Error: TAC file", args.file, "does not exist", file=sys.stderr)
    exit(1)

# Simulation data structures
builtins = ["_Alloc", "_ReadLine", "_ReadInteger", "_StringEqual", "_PrintInt", "_PrintString", "_PrintBool", "_Halt"]
tac = read_lines(args.file)
variables = {}
labels = {}
vtables = {}
stack = []
returnstack = []
# Each element of return stack is a tuple of (Return PC, Return Current Args, Return variables)
returnregister = 0
current_args = []
stringconstants = {}

# Initial pass to map labels, vtables, remove comments and whitespace, map strings
PC = 0
while PC<len(tac):
    line = tac[PC]
    line = line.replace("\n", "")
    index = 0
    label = ""
    if not line[index].isspace():
        # Parse label
        while index<len(line) and line[index]!=':' and not line[index].isspace():
            label += line[index]
            index += 1
        if label == "VTable" and line[index].isspace():
            while index<len(line) and line[index].isspace():
                index += 1
            if index==len(line):
                print("Error: no VTable name given:", line, file=sys.stderr)
                exit(1)
            VTable_name = ""
            while index<len(line) and line[index]!='=' and not line[index].isspace():
                VTable_name += line[index]
                index += 1
            if index==len(line) or not '=' in line[index:]:
                print("Error: no '=' after VTable name", line, file=sys.stderr)
                exit(1)
            if VTable_name in vtables:
                print("Error: vtable double defined:", VTable_name, file=sys.stderr)
                exit(1)
            tac[PC] = ""
            PC += 1
            index = 0
            VTable = []
            while ';' not in tac[PC]:
                VTable.append(tac[PC].strip())
                tac[PC]=""
                PC += 1
            tac[PC] = ""
            vtables[VTable_name] = VTable
            # end VTable parsing
            PC += 1
            continue
        elif index == len(line) or line[index].isspace():
            print("Error: Label not terminated:", line, file=sys.stderr)
            exit(1)
        index += 1
        if label in labels or label in builtins:
            print("Error: label double defined:", label, file=sys.stderr)
            exit(1)
        labels[label] = PC
    while index<len(line) and line[index].isspace():
        index += 1
    line = line[index:]
    index = 0
    inquote = False
    while index < len(line):
        if line[index]=='"':
            inquote = not inquote
        if not inquote and line[index]==';':
            line = line[:index]
        index += 1
    if inquote:
        print("Error: string not terminated", tac[PC], file=sys.stderr)
        exit(1)
    tac[PC] = line.strip()
    if '"' in tac[PC]:
        string = " ".join(tac[PC].split()[2:])
        if string[0] != '"' or string[-1] != '"':
            print("Error: unterminated string constant:", tac[PC], file=sys.stderr)
            exit(1)
        string = string[1:-1]
        string = string.replace("\\n", "\n")
        string = string.replace("\\r", "\r")
        string = string.replace("\\t", "\t")
        string = string.replace("\\v", "\v")
        string = string.replace("\\\"", "\"")
        string = string.replace("\\\\", "\\")
        stringconstants[PC] = string
    PC += 1

# Now run the program
if not "main" in labels:
    print("Error: No label main defined.", file=sys.stderr)
    exit(1)

PC = labels["main"]
while PC < len(tac):
    if tac[PC] != "":
        field = tac[PC].split()
        if field[0] == "BeginFunc":
            current_args = []
            if(len(field) > 2):
                formals = "".join(field[2:])
                if formals[0] != '(' or formals[-1] != ')':
                    print("Error: function arglist not enclosed in parentheses", tac[PC])
                formals = formals[1:-1]
                if formals != "":
                    current_args = formals.split(",")
            idx = 0
            while idx<len(current_args):
                if idx>=len(stack):
                    print("Error: stack empty, trying to fill", current_args[idx], file=sys.stderr)
                    exit(1)
                variables[current_args[idx]] = stack[-idx -1]
                idx += 1
        elif field[0] == "EndFunc":
            if len(returnstack) == 0:
                exit(0)
            frame = returnstack[-1]
            PC = frame[0]
            current_args = frame[1]
            # Copy modified globals
            for key in variables:
                if key not in frame[2]:
                    frame[2][key] = variables[key]
            variables = frame[2]
            returnstack.pop()
            if "=" in tac[PC]:
                print("Error: control reaches end of non-void function", file=sys.stderr)
                print(tac[PC])
                exit(1)
        elif field[0] == "Return":
            non_void = (len(field)>0)
            if tac[PC] != field[0]:
                # There is a value to return
                if len(field) > 1 and not field[1] in variables:
                    print("Error: variable", field[1], "undefined", file=sys.stderr)
                    exit(1)
                if len(field) > 1:
                    returnregister = variables[field[1]]
            if len(returnstack) == 0:
                exit(0)
            frame = returnstack[-1]
            PC = frame[0]
            current_args = frame[1]
            # Copy modified globals
            for key in variables:
                if key not in frame[2]:
                    frame[2][key] = variables[key]
            variables = frame[2]
            returnstack.pop()
            if "=" in tac[PC]:
                field = tac[PC].split()
                if not non_void:
                    print("Error:", field[3], "does not return a value", file=sys.stderr)
                    print(tac[PC])
                    exit(1)
                variables[field[0]] = returnregister
        elif field[0] == "Goto":
            if len(field) == 1:
                print("Error: no label listed after goto", file=sys.stderr)
                exit(1)
            if field[1] not in labels:
                print("Error: No label", field[1], "defined.", file=sys.stderr)
                exit(1)
            PC = labels[field[1]] - 1 # To offset += 1 at the end
        elif field[0] == "IfZ":
            if len(field) <= 3 or field[2] != "Goto":
                print("Error: no goto after IfZ:", tac[PC], file=sys.stderr)
                exit(1)
            if not field[1] in variables:
                print("Error: variable", field[1], "undefined", file=sys.stderr)
                exit(1)
            if variables[field[1]] == 0:
                if len(field) != 4:
                    print("Error: No label listed after goto", file=sys.stderr)
                if field[3] not in labels:
                    print("Error: No label", field[3], "defined.", file=sys.stderr)
                    exit(1)
                PC = labels[field[3]] - 1 # To offset += 1 at the end
        elif field[0] == "PushParam":
            if len(field) == 1:
                print("Error: no param specified to push", file=sys.stderr)
                exit(1)
            if not field[1] in variables:
                print("Error: variable", field[1], "undefined", file=sys.stderr)
                exit(1)
            stack.append(variables[field[1]])
        elif field[0] == "PopParams":
            for i in range(int(field[1])//4):
                stack.pop()
        elif field[0] == "LCall":
            if len(field) == 1:
                print("Error: No label listed after LCall", file=sys.stderr)
                exit(1)
            if not field[1] in labels and field[1] not in builtins:
                print("Error: No label", field[1], "defined.", file=sys.stderr)
                exit(1)
            if field[1] in labels:
                frame = (PC, current_args, variables.copy())
                returnstack.append(frame)
                PC = labels[field[1]] - 1 # To offset += 1 at the end
            else:
                #builtins
                if field[1] == "_Halt":
                    exit(0)
                elif field[1] == "_PrintString" or field[1] == "_PrintInt":
                    if(len(stack)) == 0:
                        print("Error: stack empty, trying to fill Print argument", file=sys.stderr)
                        exit(1)
                    print(stack[-1], end="")
                elif field[1] == "_PrintBool":
                    if(len(stack)) == 0:
                        print("Error: stack empty, trying to fill Print argument", file=sys.stderr)
                        exit(1)
                    if stack[-1] == 0:
                        print("False", end="")
                    else:
                        print("True", end="")
                elif field[1] == "_ReadLine":
                    returnregister = input()
                elif field[1] == "_ReadInteger":
                    returnregister = int(input())
                elif field[1] == "_StringEqual":
                    if(len(stack)) <= 1:
                        print("Error: stack empty, trying to fill strcmp argument", file=sys.stderr)
                        exit(1)
                    returnregister = int(stack[-1] == stack[-2])
                elif field[1] == "_Alloc":
                    if(len(stack)) == 0:
                        print("Error: stack empty, trying to fill Alloc argument", file=sys.stderr)
                        exit(1)
                    returnregister = [None] * (stack[-1]//4 - 1) + [stack[-1]//4 - 1]
        elif PC in stringconstants:
            variables[field[0]] = stringconstants[PC]
        elif field[0][0:2] == '*(':
            offset = 0
            field[0] = field[0][2:]
            if field[0][-1] == ')':
                # No offset in the deference
                field[0] = field[0][:-1]
                if len(field) != 3 or field[1] != "=":
                    print("Error: bad syntax for store", tac[PC], file=sys.stderr)
            else:
                if len(field) != 5 or field[2][-1] != ')' or field[1] != "+" or field[3] != "=":
                    print("Error: bad syntax for store", tac[PC], file=sys.stderr)
                offset = int(field[2][:-1])//4
                field[2] = field[4]
            if field[0] not in variables:
                print("Error: variable", field[0], "undefined", file=sys.stderr)
                exit(1)
            if field[2] not in variables:
                print("Error: variable", field[2], "undefined", file=sys.stderr)
                exit(1)
            if type(variables[field[0]]) == list:
                variables[field[0]][offset] = variables[field[2]]
            elif type(variables[field[0]]) == tuple:
                variables[field[0]][0][offset + variables[field[0]][1]//4] = variables[field[2]]
        elif len(field) < 3 or field[1] != "=":
            print("Error: unrecognized instruction:", tac[PC], file=sys.stderr)
            exit(1)
        else:
            # At least 3 fields and field 1 is =
            if field[2] == "LCall":
                if len(field) != 4:
                    print("Error: No label listed after LCall", file=sys.stderr)
                    exit(1)
                if not field[3] in labels and field[3] not in builtins:
                    print("Error: No label", field[3], "defined.", file=sys.stderr)
                    exit(1)
                if field[3] in labels:
                    frame = (PC, current_args, variables.copy())
                    returnstack.append(frame)
                    PC = labels[field[3]] - 1 # To offset += 1 at the end
                else:
                    #builtins
                    if field[3] == "_Halt":
                        exit(0)
                    elif field[3] == "_PrintString" or field[3] == "_PrintInt":
                        if(len(stack)) == 0:
                            print("Error: stack empty, trying to fill Print argument", file=sys.stderr)
                            exit(1)
                        print(stack[-1], end="")
                        print("Error:", field[3], "does not return a value", file=sys.stderr)
                        exit(1)
                    elif field[3] == "_PrintBool":
                        if(len(stack)) == 0:
                            print("Error: stack empty, trying to fill Print argument", file=sys.stderr)
                            exit(1)
                        if stack[-1] == 0:
                            print("False", end="")
                        else:
                            print("True", end="")
                    elif field[3] == "_ReadLine":
                        variables[field[0]] = input()
                    elif field[3] == "_ReadInteger":
                        variables[field[0]] = int(input())
                    elif field[3] == "_StringEqual":
                        if(len(stack)) <= 1:
                            print("Error: stack empty, trying to fill strcmp argument", file=sys.stderr)
                            exit(1)
                        variables[field[0]] = int(stack[-1] == stack[-2])
                    elif field[3] == "_Alloc":
                        if(len(stack)) == 0:
                            print("Error: stack empty, trying to fill Alloc argument", file=sys.stderr)
                            exit(1)
                        variables[field[0]] = [None] * (stack[-1]//4 - 1) + [stack[-1]//4 - 1]
                    else:
                        print("Error: missing builtin", field[3], file=sys.stderr)
            if len(field) == 3 and field[2][:2] != "*(":
                # Simple assign
                if field[2][0] >= '0' and field[2][0] <= '9':
                    variables[field[0]] = int(field[2])
                else:
                    if field[2] not in variables:
                        print("Error: variable", field[2], "undefined", file=sys.stderr)
                        exit(1)
                    variables[field[0]] = variables[field[2]]
            elif len(field) == 3:
                if field[2][-1] != ")":
                    print("Error: bad syntax for load", tac[PC], file=sys.stderr)
                    exit(1)
                field[2] = field[2][2:-1]
                if field[2] not in variables:
                    print("Error: variable", field[2], "undefined", file=sys.stderr)
                    print(PC)
                    exit(1)
                if type(variables[field[2]]) == list:
                    variables[field[0]] = variables[field[2]][0]
                elif type(variables[field[2]]) == tuple:
                    variables[field[0]] = variables[field[2]][0][variables[field[2]][1]//4]
            if len(field) > 5:
                print("Error: bad syntax", tac[PC], file=sys.stderr)
                exit(1)
            if len(field) == 5 and field[2][0:2] == "*(":
                if field[4][-1] != ")" or field[3] != "+":
                    print("Error: bad syntax for load", tac[PC], file=sys.stderr)
                    exit(1)
                field[2] = field[2][2:]
                field[4] = field[4][:-1]
                if field[2] not in variables:
                    print("Error: variable", field[2], "undefined", file=sys.stderr)
                    exit(1)
                if type(variables[field[2]]) == list:
                    variables[field[0]] = variables[field[2]][int(field[4])//4]
                elif type(variables[field[2]]) == tuple:
                    variables[field[0]] = variables[field[2]][0][variables[field[2]][1]//4 + int(field[4])//4]
            elif len(field) == 5:
                if field[3] not in ["+", "-", "*", "/", "%", "==", "<", "&&", "||"]:
                    print("Error: invalid binary operation", tac[PC], file=sys.stderr)
                if field[2] not in variables:
                    print("Error: variable", field[2], "undefined", file=sys.stderr)
                    exit(1)
                if field[4] not in variables:
                    print("Error: variable", field[4], "undefined", file=sys.stderr)
                    exit(1)
                if field[3] == "+":
                    if(type(variables[field[2]]) == int and type(variables[field[4]]) == int):
                        variables[field[0]] = variables[field[2]] + variables[field[4]]
                    if(type(variables[field[2]]) == list and type(variables[field[4]]) ==  int):
                        variables[field[0]] = (variables[field[2]], variables[field[4]])
                    if(type(variables[field[2]]) == int and type(variables[field[4]]) ==  list):
                        variables[field[0]] = (variables[field[4]], variables[field[2]])
                    if(type(variables[field[2]]) == tuple and type(variables[field[4]]) ==  int):
                        variables[field[0]] = (variables[field[2]][0], variables[field[2]][1] + variables[field[4]])
                    if(type(variables[field[2]]) == int and type(variables[field[4]]) ==  tuple):
                        variables[field[0]] = (variables[field[4]][0], variables[field[4]][1] + variables[field[0]])
                if field[3] == "-":
                    variables[field[0]] = variables[field[2]] - variables[field[4]]
                if field[3] == "*":
                    variables[field[0]] = variables[field[2]] * variables[field[4]]
                if field[3] == "/":
                    variables[field[0]] = variables[field[2]] // variables[field[4]]
                if field[3] == "%":
                    variables[field[0]] = variables[field[2]] % variables[field[4]]
                if field[3] == "==":
                    variables[field[0]] = int(variables[field[2]] == variables[field[4]])
                if field[3] == "<":
                    variables[field[0]] = int(variables[field[2]] < variables[field[4]])
                if field[3] == "&&":
                    variables[field[0]] = int(variables[field[2]] and variables[field[4]])
                if field[3] == "||":
                    variables[field[0]] = int(variables[field[2]] or variables[field[4]])
    PC += 1
print("Error: End of TAC file reached without halt", file=sys.stderr)
exit(1)