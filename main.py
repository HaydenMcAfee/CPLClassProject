# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

from plex import *

from PascalInterpreter import PascalInterpreter
from PascalScanner import PascalScanner
filename = "program_file.txt"

def __main__():

    f = open(filename, "r")

    # perform lexical and syntax checking
    # maybe convert to intermediate form
    # execute it
    scanner = PascalScanner(f, filename)

    # scanner2.doScanner()

    interpreter = PascalInterpreter(scanner)
    interpreter.Execute()


    # print('interpreting')
    # interpreter = PascalInterpreter()
    # interpreter.doInterpreter(scanner)
__main__()
