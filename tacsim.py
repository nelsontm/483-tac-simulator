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
tac = read_lines(args.file)
variables = {}
labels = {}
vtables = {}
stack = []
returnstack = []
returnregister = 0

# Initial pass to map labels, vtables, remove comments and whitespace
PC = 0
def_VTable = False
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
        if label in labels:
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
for line in tac:
    print(line)