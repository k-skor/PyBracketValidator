#!/usr/bin/python

import sys

class Bracket:
    def __init__(self):
        print("++ Bracket ++")
        self.startIdx_ = 0
        self.endIdx_ = 0

    def empty(self):
        return self.startIdx_ == 0 and self.endIdx_ == 0

    def open(self,startIdx):
        self.startIdx_ = startIdx

    def close(self,endIdx):
        self.endIdx_ = endIdx

class DefaultBracket(Bracket):
    pass

class CurlyBracket(Bracket):
    pass

def validate(expr):
    startIdx = 0;
    endIdx = len(expr) - 1
    defaultBracketCheck = Bracket()
    curlyBracketCheck = Bracket()
    print("end idx: {}").format(endIdx)
    while (startIdx != endIdx):
        if expr[startIdx] == "(":
            defaultBracketCheck.open(startIdx)
        elif expr[endIdx] == ")":
            if not curlyBracketCheck.empty():
                break
            defaultBracketCheck.close(endIdx)

        if expr[startIdx] == "{":
            curlyBracketCheck.open(startIdx)
        elif expr[endIdx] == "}":
            if not defaultBracketCheck.empty():
                break
            curlyBracketCheck.close(endIdx)

        if defaultBracketCheck.empty() and defaultBracketCheck.empty():
            startIdx = startIdx + 1
        else:
            endIdx = endIdx - 1
        

def main():
    print("args: {}").format(sys.argv)
    validate(sys.argv[1])

if __name__ == "__main__":
    main()
