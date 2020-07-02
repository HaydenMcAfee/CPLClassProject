from plex import *

from PascalScanner import PascalScanner
from PascalParser import PascalParser
from PascalInterpreter import PascalInterpreter




filename = "program_file.txt"


def __main__():

    f = open(filename, "r")

    # perform lexical and syntax checking
    # maybe convert to intermediate form
    # execute it
    print('scanning')
    scanner = PascalScanner(f, filename)

    print('parsin')
    parser = PascalParser(scanner)
    parser.doParser()

    # print('interpreting')
    # interpreter = PascalInterpreter()
    # interpreter.doInterpreter(scanner)
__main__()
