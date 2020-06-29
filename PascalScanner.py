from plex import *

# The assignment of each set of valid inputs for each token type
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

scanner = Scanner(lexicon, f, filename)
while 1:
    token = scanner.read()
    # The .read() function will return a tuple with the token and string and then their line and start column will be concatened to the output
    print str(token) + ": line: " + str(scanner.cur_line) + " col: " + str(scanner.start_col)
    if token[0] is None:
        break