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
# Each element of return stack is a tuple of (Return PC, Return Current Args, Return Variables)
returnregister = 0
current_args = []

# Initial pass to map labels, vtables, remove comments and whitespace
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
            line = line[:index-1]
        index += 1
    if inquote:
        print("Error: string not terminated", tac[PC], file=sys.stderr)
        exit(1)
    tac[PC] = line.strip()
    PC += 1

# Now run the program
if not "main" in labels:
    print("Error: No label main defined.", file=sys.stderr)
    exit(1)

PC = labels["main"]
while PC < len(tac):
    if tac[PC] != "":
        index = 0
        field0 = ""
        while index<len(tac[PC]) and not tac[PC][index].isspace():
            field0 += tac[PC][index]
            index += 1
        if field0 == "BeginFunc":
            current_args = []
            while index<len(tac[PC]) and not tac[PC][index] == '(':
                index += 1
            index += 1
            arg = ""
            while index<len(tac[PC]) and not tac[PC][index] == ')':
                if tac[PC][index] == ',':
                    current_args.append(arg)
                    arg = ""
                elif not tac[PC][index].isspace():
                    arg += tac[PC][index]
                index += 1
            if index == len(tac[PC]):
                print("Error: argslist not terminated:", tac[PC], file=sys.stderr)
                exit(1)
            if arg != "":
                current_args.append(arg)
            idx = 0
            while idx<len(current_args):
                variables[current_args[idx]] = stack[-idx -1]
                idx += 1
        elif field0 == "EndFunc":
            if len(returnstack) == 0:
                exit(0)
            frame = returnstack[-1]
            PC = frame[0]
            current_args = frame[1]
            variables = frame[2]
            returnstack.pop()
            if "=" in tac[PC]:
                print("Error: control reaches end of non-void function", file=sys.stderr)
                exit(1)
        elif field0 == "Return":
            non_void = (tac[PC] != field0)
            if tac[PC] != field0:
                # There is a value to return
                index += 1
                field1 = ""
                while index<len(tac[PC]) and not tac[PC][index].isspace():
                    field1 += tac[PC][index]
                    index += 1
                if not field1 in variables and field1 != "":
                    print("Error: variable", field1, "undefined", file=sys.stderr)
                    exit(1)
                if field1 != "":
                    returnregister = variables[field1]
            if len(returnstack) == 0:
                exit(0)
            frame = returnstack[-1]
            PC = frame[0]
            current_args = frame[1]
            variables = frame[2]
            returnstack.pop()
            if "=" in tac[PC]:
                if non_void:
                    print("Error: control reaches end of non-void function", file=sys.stderr)
                    exit(1)
                index = 0
                field0 = ""
                while index<len(tac[PC]) and not tac[PC][index].isspace():
                    field0 += tac[PC][index]
                    index += 1
                variables[field0] = returnregister
        elif field0 == "Goto":
            index += 1
            if not tac[PC][index:] in labels:
                print("Error: No label", tag[PC][index:], "defined.", file=sys.stderr)
                exit(1)
            field1 = tac[PC][index:]
            if field1 not in labels:
                print("Error: No label", field3, "defined.", file=sys.stderr)
                exit(1)
            PC = labels[field1] - 1 # To offset += 1 at the end
        elif field0 == "IfZ":
            index += 1
            field1 = ""
            while index<len(tac[PC]) and not tac[PC][index].isspace():
                field1 += tac[PC][index]
                index += 1
            if index == len(tac[PC]):
                print("Error: no goto after IfZ:", tac[PC], file=sys.stderr)
                exit(1)
            if not field1 in variables:
                print("Error: variable", field1, "undefined", file=sys.stderr)
                exit(1)
            if variables[field1] == 0:
                field2 = ""
                while index<len(tac[PC]) and not tac[PC][index].isspace():
                    field2 += tac[PC][index]
                    index += 1
                if index == len(tac[PC]):
                    print("Error: no goto after IfZ:", tac[PC], file=sys.stderr)
                    exit(1)
                index += 1
                field3 = tac[PC][index:]
                if field3 not in labels:
                    print("Error: No label", field3, "defined.", file=sys.stderr)
                    exit(1)
                PC = labels[field3] - 1 # To offset += 1 at the end
        elif field0 == "PushParam":
            index += 1
            field1 = tac[PC][index:]
            if field1 == "":
                print("Error: no param specified to push", file=sys.stderr)
                exit(1)
            if not field1 in variables:
                print("Error: variable", field1, "undefined", file=sys.stderr)
                exit(1)
            stack.append(variables[field1])
        elif field0 == "PopParams":
            index += 1
            field1 = tac[PC][index:]
            field1 = int(field1) / 4
            for i in range(field1):
                stack.pop()
    PC += 1
print("Error: End of TAC file reached without halt", file=sys.stderr)
exit(1)