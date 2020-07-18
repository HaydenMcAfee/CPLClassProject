# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

from plex import *
from IdentifierTable import IdentifierTable

class PascalParser(object):

    # Uses and Pascal scanner object as a parameter to be used during parsing
    def __init__(self, scanner, inter):
        self.scanner = scanner
        # Idtable object created for management of identifiers in the parsing of tokens
        self.inter = inter

    # Checks the file for correct syntax and throws exceptions if there are any issues
    def doParser(self):
        token = self.scanner.nextToken()
        self.programNameCheck(token) # Will check if the program is named
        token = self.scanner.nextToken()
        self.loadImports(token) # Will load imports if there are any and also look for keyword begin or else parse will fail
        token = self.scanner.nextToken()
        self.checkBeg(token)
        # Begin checking body of program
        while 1:
            token = self.scanner.nextToken()
            # Check if we are at the end of the program or block
            if self.checkEnd(token):
                token = self.scanner.nextToken()
                if not self.endOfStatement(token):
                    break
                else:
                    self.checkBeg(token)
            # Will continue to read until token is none which means the end of the file has been reached
            else:
                # We are in the body of the program or block, but we need to make sure we are not at the end of file
                # If we are not at the end of the file then parse the next token
                if token[0] is None:
                    raise NameError("No end keyword at end of program")
                self.parseToken(token)

    # Handles the token if it is a function, keyword, or identifier
    def parseToken(self, token):
        if token[0] == 'function':
            self.handleFunction(token)
        if token[0] == 'keyword':
            self.handleKeyword(token)
        if token[0] == 'identifier':
            self.handleIdentifier(token)
        if token[0] == 'literal' or 'integer':
            self.handleValue(token)

    # Handles the token when type is identifier
    def handleIdentifier(self, token):
        self.interpretToken(token) # Handles whether to initialize the identifier
        token = self.scanner.nextToken()
        self.interpretToken(token)

    def handleValue(self, token):
        self.interpretToken(token)





    # Only boolean, doesn't throw exceptions
    def endOfStatement(self, token):
        if token[1] == ";":
            return True
        else:
            return False

    # We want to check if the program keyword is used and the following token is an identifier but not to store it
    def programNameCheck(self, token):
        if token[1] == 'program':
            self.interpretToken(token)
            token = self.scanner.nextToken()
            if token[0] == 'identifier':
                self.interpretToken(token)
                token = self.scanner.nextToken()
                if self.endOfStatement(token): # Check for ;
                    return
                else:
                    raise NameError("Invalid end of statement, expected ;")
            else:
                raise NameError('Program name not valid')
        else:
            raise NameError("Program name not declared")

    # Checks the validity of import statements at the top of program
    def loadImports(self, token):
        while token[1] != 'begin':
            if token[1] == 'uses': # Program not set to begin, so we check if there's an import keyword
                self.interpretToken(token)
                token = self.scanner.nextToken()
                if token[0] == 'identifier': # Triggers fail if library name is not valid
                    self.interpretToken(token)
                    token = self.scanner.nextToken()
                    if self.endOfStatement(token):  # Check for ;
                        return
                    else:
                        raise NameError("Invalid end of statement, expected ;")
                else:
                    raise NameError("Invalid library name")
            else: # Triggers a fail if the import statement is not valid
                raise NameError("Expected an import keyword")
        # No imports to load and program has begin keyword
        return

    # Checks if there is an end keyword and if its the end of the program or block
    # Returns True if end of program, False if end of block, Excepts on anything else
    def checkEnd(self, token):
        if token[1] == "end":
            token = self.scanner.nextToken()
            if token[1] == '.':
                return True
            if token[0] is None:
                raise NameError('Expected . after end keyword')
            if token[1] != ';':
                raise NameError('Expected ; or . after end keyword')

    # Since the end token is not an end. then check for the beginning of another program block
    def checkBeg(self, token):
        if token[1] == "begin":
            self.interpretToken(token)
            return True
        else:
            raise NameError('Expected begin keyword')

    # Handles a function and checks the syntax of the sentence it is used in
    def handleFunction(self, token):
        token = self.scanner.nextToken()
        self.checkOpenParens(token)
        token = self.scanner.nextToken()
        self.checkParam(token)
        token = self.scanner.nextToken()
        self.checkCloseParens(token)
        token = self.scanner.nextToken()
        self.endOfStatement(token)

    # Checks for (
    def checkOpenParens(self, token):
        if token[1] != '(':
            raise NameError('Expected (')

    # Checks for )
    def checkCloseParens(self, token):
        if token[1] != ')':
            raise NameError('Expected )')

    # Checks if parameter is valid
    def checkParam(self, token):
        if token[0] == 'keyword':
            raise NameError('Invalid Parameter')

    # Handles a keyword and checks the syntax of the sentence it is used in
    def handleKeyword(self, token):
        token = self.scanner.nextToken()
        if not self.endOfStatement(token):
            raise NameError('Expected ; after keyword')

    # Calls the interpreter class for the execution of the instruction
    def interpretToken(self, token):
        # Our actual token
        name = token[1]
        # The tokens type
        tType = token[0]
        # Call the interpret method with the name, type and idtable
        self.inter.Interpret(name, tType, self.idtable)



