#!/usr/bin/python

import sys

bracketChars = "(){}"

class BracketPair:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            return False
        self.opened = True
        return True

    def close(self):
        if not self.opened:
            return False
        self.opened = False
        return True

class DefaultBracketPair(BracketPair):
    def handleBracket(self, char):
        if char == "(":
            return self.open()
        elif char == "{":
            return False
        elif char == ")":
            return self.close()
        elif char == "}":
            return False

class CurlyBracketPair(BracketPair):
    def handleBracket(self, char):
        if char == "(":
            return False
        elif char == "{":
            return self.open()
        elif char == ")":
            return False
        elif char == "}":
            return self.close()

def handleChar(char):
    if char == "(" or char == ")":
        return DefaultBracketPair()
    elif char == "{" or char == "}":
        return CurlyBracketPair()
    else:
        return None

def validate(expr):
    startIdx = 0;
    endIdx = len(expr)
    brPair = None
    idx = 0
    while (startIdx != endIdx):

        if expr[idx] in bracketChars:
            if brPair is None or not brPair.opened:
                brPair = handleChar(expr[idx])
            if brPair is not None:
                if not brPair.handleBracket(expr[idx]):
                    return False

        if brPair is None or not brPair.opened:
            startIdx = startIdx + 1
            idx = startIdx
        else:
            endIdx = endIdx - 1
            idx = endIdx
    return True


def main():
    ret = validate(sys.argv[1])
    print(ret)
    return ret

if __name__ == "__main__":
    main()
