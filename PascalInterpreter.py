# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

# Class for future use
from PascalParser import PascalParser
from IdentifierTable import IdentifierTable


class PascalInterpreter():

    def __init__(self, scanner):
        self.idTable = IdentifierTable()
        self.parser = PascalParser(scanner, self)
        self.initState = 0 # Used to execute initiating tokens
        self.bodyState = 0 # Used to execute body tokens
        self.curIdent = "";

    def Execute(self):
        self.parser.doParser()
        print("Executed")

    def Interpret(self, token, tType):
        # print("interpreting" +str(token))
        # For an interpreter:
        if self.initState < 3:
            self.programHead(token, tType)
        else:
            if tType == "identifier":
                self.checkIdentifier(token) # Stores identifier name if not in table
                self.curIdent = token
            elif self.bodyState == 1:
                if token == '=':
                    self.bodyState = 2
            elif self.bodyState == 2:
                self.setIdentifierValue(token)
                self.bodyState = 0
                
                
                    
                
    def programHead(self, token, tType):
        if token == "program":
            self.initState = 1  # Changes the initState to 1 since next token is the program name
        elif self.initState == 1:  # Displays what program we are executing
            print("Executing " + str(token))
            self.initState = 0
        elif token == "uses":  # Sets initState 2 for loading the library
            self.initState = 2
        elif self.initState == 2:  # Prints the name of the library being used
            print("Loading library " + str(token))
        elif token == "begin":
            self.initState = 3
                
                
                    

    # Stores the identifier if there it is not in the table
    def checkIdentifier(self, token):
        if not self.idTable.lookup(token):
            self.idTable.store(token)
            self.bodyState = 1

    def setIdentifierValue(self, token):
        pass





