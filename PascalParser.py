from plex import *

class PascalParser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def doParser(self):

        if self.programNameCheck(): # Will check if the program is named
            if self.loadImports(): # Will load imports if there are any and also look for keyword begin or else parse will fail
                while 1:
                    token = self.scanner.nextToken()
                    # Will continue to read until token is none which means the end of the file has been reached
                    if token[0] is None:
                        break
                    self.parseToken(token)
                print('Parsed!')


    def parseToken(self, token):
        pass

    def endOfStatement(self, token):
        if token[1] == ";":
            return True
        else:
            print("Invalid end of statement, expected ;")
            return False

    # We want to check if the program keyword is used and the following token is an identifier but not to store it
    def programNameCheck(self):
        token = self.scanner.nextToken()
        if token[1] == 'program':
            token = self.scanner.nextToken()
            if token[0] == 'identifier':
                token = self.scanner.nextToken()
                if self.endOfStatement(token): # Check for ;
                    return True
            else:
                print("Program name not valid")
                return False
        else:
            print("Program name not declared")
            return False

    def loadImports(self):
        token = self.scanner.nextToken()
        while token[1] != 'begin':
            if token[1] == 'uses': # Program not set to begin, so we check if there's an import keyword
                token = self.scanner.nextToken()
                if token[0] == 'identifier': # Triggers fail if library name is not valid
                    token = self.scanner.nextToken()
                    if self.endOfStatement(token):  # Check for ;
                        return True
                else:
                    print("Invalid library name")
                    return False
            else: # Triggers a fail if the import statement is not valid
                print("Expected an import keyword")
                return False
        # No imports to load and program has begin keyword
        return True

    def handleIdentfier(self):
        pass


