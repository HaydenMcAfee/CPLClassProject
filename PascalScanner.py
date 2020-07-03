from plex import *
from IdentifierTable import IdentifierTable

class PascalScanner():
    idtable = IdentifierTable()
        # The assignment of each set of valid inputs for each token type
    def __init__(self, f, filename):
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
        string = Str("'") + Rep(AnyBut("'")) + Str("'")
        keyword = Str("as", "class", "dispinterface", "except", "exports", "finalization", "finally", "program",
                      "initialization", "inline", "is", "library", "on", "out", "packed", "property", "readkey",
                      "raise", "resourcestring", "threadvar", "try", "if", "then", "else", "begin", "end", "for", "or", "uses")
        func = Str("writeln")


        # Creation of the lexicon for use later in the scanner
        lexicon = Lexicon([
            (keyword, 'keyword'), # Handles the keyword table and will find if token is a keyword
            (func, 'function'),
            (strng, 'literal'),
            (name, 'identifier'),
            (int, 'integer'),
            (space | comment, IGNORE),
            (string, 'string'),
            (symbol, 'symbol')
        ])

        self.scanner = Scanner(lexicon, f, filename)

    def nextToken(self):
        return self.scanner.read()

    def doScanner(self):
        while 1:
            token = self.nextToken()
            # The .read() function will return a tuple with the token and string and then their line and start column will be concatened to the output
            if token[0] is None:
                break
            self.idtable.store(str(token) + ": line: " + str(self.scanner.cur_line) + " col: " + str(self.scanner.start_col))
            self.idtable.getAll()
