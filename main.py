from plex import *

from PascalScanner import PascalScanner
from PascalInterpreter import PascalInterpreter

# The assignment of each set of valid inputs for each token type
def __main__():
    letter = Range("AZaz")
    digit = Range("09")
    name = letter + Rep(letter | digit)
    int = Rep1(digit)
    space = Any(" \t\n")
    comment = Str("(*") + Rep(AnyBut("*)")) + Str("*)")
    symbol = Str("+", "*", "/", "=", "<",  ">", "[", "]", ".", "(", ")", ":",
                    "^",  "@",  "{",  "}",  "$",  "#", "<=", ">=",
                    ":=", "+=", "-=", "*=", "/=", "(* *)", "(. .)", "//", ";")
    string = Str("'") + Rep(AnyBut("'")) + Str("'")
    resword = Str("as", "class"  ,"dispinterface", "except",  "exports",  "finalization",  "finally",
                    "initialization",  "inline",  "is",  "library",  "on", "out",  "packed",  "property",
                    "raise",  "resourcestring",  "threadvar",  "try", "if", "then", "else", "end", "for", "or")

    # Creation of the lexicon for use later in the scanner
    lexicon = Lexicon([
        (name,              'identifier'),
        (int,               'integer'),
        (space | comment,   IGNORE),
        (string,           'string'),
        (resword,           'resword'),
        (symbol,            'symbol')
    ])

    filename = "program_file.txt"
    f = open(filename, "r")

    # perform lexical and syntax checking
    # maybe convert to intermediate form
    # execute it
    print('scanning')
    scanner = PascalScanner()
    scanner.doScanner(lexicon, f, filename)

    print('interpreting')
    interpreter = PascalInterpreter()
    interpreter.doInterpreter()
__main__()
