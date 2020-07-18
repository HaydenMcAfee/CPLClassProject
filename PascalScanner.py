# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

from plex import *

class PascalScanner():

    # All the variables are use to create the attribute scanner of the class
    def __init__(self, f, filename):
        bool = Str("false", "true")
        letter = Range("AZaz")
        digit = Range("09")
        name = letter + Rep(letter | digit)
        int = Rep1(digit)
        strng = Str("'") + Rep(AnyBut("'")) + Str("'")
        space = Any(" \t\n")
        comment = Str("(*") + Rep(AnyBut("*)")) + Str("*)")
        symbol = Str("+", "*", "/", "=", "<", ">", "[", "]", ".", "(", ")", ":",
                     "^", "@", "{", "}", "$", "#", "<=", ">=",
                     ":=", "+=", "-=", "*=", "/=", "(* *)", "(. .)", "//", ";")
        # string = Str("'") + Rep(AnyBut("'")) + Str("'")
        keyword = Str("as", "class", "dispinterface", "except", "exports", "finalization", "finally", "program",
                      "initialization", "inline", "is", "library", "on", "out", "packed", "property", "readkey",
                      "raise", "resourcestring", "threadvar", "try", "if", "then", "else", "begin", "end", "for", "or", "uses")
        func = Str("writeln")


        # Creation of the lexicon for use later in the scanner
        lexicon = Lexicon([
            (bool, 'boolean'),
            (keyword, 'keyword'), # Handles the keyword table and will find if token is a keyword
            (func, 'function'),
            (strng, 'literal'),
            (name, 'identifier'),
            (int, 'integer'),
            (space | comment, IGNORE),
            # (string, 'string'),
            (symbol, 'symbol')
        ])

        self.scanner = Scanner(lexicon, f, filename)
        self.initial = Scanner(lexicon, f, filename)

    # Returns the next valid token in the file
    def nextToken(self):
        return self.scanner.read()

    # Demos scanner and prints the scanned tokens with their labels
    def doScanner(self):
        initial = self.scanner.initial_state
        while 1:
            token = self.nextToken()
            # The .read() function will return a tuple with the token and string and then their line and start column will be concatened to the output
            if token[0] is None:
                self.scanner.begin(initial)
                break
            print(str(token) + ": line: " + str(self.scanner.cur_line) + " col: " + str(self.scanner.start_col))


