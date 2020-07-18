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
        self.initState = 0 # Used to in initiating the program
        self.bodyState = 0 # Used to execute body tokens
        self.curIdent = None
        self.functionStack = []

    def Execute(self):
        self.parser.doParser()
        print("Executed")

    def Interpret(self, token, tType):
        # print("interpreting" +str(token))
        # For an interpreter:
        if self.initState <= 2:
            self.programHead(token, tType)
        elif self.initState == 3:
            if self.bodyState == 0 and tType == "identifier":
                self.storeIdent(token)
                return
            elif self.bodyState == 1: # sets the body state to 2 for assignment of next token
                self.checkOp(token)
                return
            elif self.bodyState == 2: # Assigns the token value to the current identifier
                self.storeValue(token,tType)
                return
            elif tType == 'function':
                self.bodyState = 4 # Setting body state to 4 because there is a function on the stack
                self.functionStack.append(token)
                return
            elif self.bodyState == 4: # Execute the function stack
                self.executeFunctionStack(token, tType)


    # Stores the indentifier if not already created
    def storeIdent(self, token):
        # Token needs to either set a value for an identifier or return the value of
        # the indentifier
        self.checkIdentifier(token)  # Stores identifier name if not in table
        self.curIdent = token  # We store the value of the current Identifier for later functions]

    # checks the operator
    def checkOp(self, token):
        if token == '=':
            self.bodyState = 2
            return True
        else:
            return False


    # Handles interpretation of the program head containing the program statement and libraries
    def programHead(self, token, tType):
        if token == "program":
            self.initState = 1  # Changes the initState to 1 since next token is the program name
        elif self.initState == 1:  # Displays what program we are executing
            print("Executing " + str(token))
            self.initState = 0
        elif token == "uses":  # Sets initState 2 for loading the library
            self.initState = 2
        elif token == "begin":
            self.initState = 3
        elif self.initState == 2:  # Prints the name of the library being used
            print("Loading library " + str(token))


    # Stores the identifier if there it is not in the table
    def checkIdentifier(self, token):
        if not self.idTable.lookup(token):
            self.idTable.store(token)
            self.bodyState = 1

    # Sets the current identifier's value to the value found in the token's tuple
    def setIdentifierValue(self, token, tType):
        self.idTable.storeVal(self.curIdent, token, tType)

    # Stores the value of the token to the current identifier
    def storeValue(self, token, tType):
        if token == 'readkey':  # allows us to run the readkey and take input for the identifier value
            token = input("Enter input")
            if type(token) == int: # Determines our input's type
                tType = 'integer'
            elif token == 'true' or 'false':
                tType = 'boolean'
            else:
                tType = 'literal'
        self.setIdentifierValue(token, tType)
        self.curIdent = None
        self.parser.checkSemiFlag = True
        self.bodyState = 0

    def executeFunctionStack(self, token, tType):
        for func in self.functionStack:
            function = self.functionStack.pop()
            if function == 'writeln':
                if tType == 'identifier':  # Allows us to getvalue of the identifier parameter
                    if not self.idTable.lookup(token):
                        raise NameError('Value not initialized')
                    token = self.idTable.getVal(token)
                    tType = self.idTable.getType(token)
                if tType == 'literal':
                    print(token[1:-1])
                else:
                    print(token)
                self.bodyState = 0





