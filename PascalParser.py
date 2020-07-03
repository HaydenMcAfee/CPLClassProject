from plex import *

class PascalParser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def doParser(self):
        token = self.scanner.nextToken()
        if self.programNameCheck(token): # Will check if the program is named
            token = self.scanner.nextToken()
            if self.loadImports(token): # Will load imports if there are any and also look for keyword begin or else parse will fail
                token = self.scanner.nextToken()
                self.checkBeg(token)
                while 1:
                    token = self.scanner.nextToken()
                    if self.checkEnd(token):
                        token = self.scanner.nextToken()
                        if not self.endOfStatement(token):
                            break
                        else:
                            self.checkBeg(token)


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
            return False

    # We want to check if the program keyword is used and the following token is an identifier but not to store it
    def programNameCheck(self, token):
        if token[1] == 'program':
            token = self.scanner.nextToken()
            if token[0] == 'identifier':
                token = self.scanner.nextToken()
                if self.endOfStatement(token): # Check for ;
                    return True
                else:
                    raise NameError("Invalid end of statement, expected ;")
            else:
                raise NameError('Program name not valid')
        else:
            raise NameError("Program name not declared")

    def loadImports(self, token):
        while token[1] != 'begin':
            if token[1] == 'uses': # Program not set to begin, so we check if there's an import keyword
                token = self.scanner.nextToken()
                if token[0] == 'identifier': # Triggers fail if library name is not valid
                    token = self.scanner.nextToken()
                    if self.endOfStatement(token):  # Check for ;
                        return True
                    else:
                        raise NameError("Invalid end of statement, expected ;")
                else:
                    raise NameError("Invalid library name")
            else: # Triggers a fail if the import statement is not valid
                raise NameError("Expected an import keyword")
        # No imports to load and program has begin keyword
        return True

    def handleIdentfier(self):
        pass

    # Checks if there is an end keyword and if its the end of the program or block
    # Returns True if end of program, False if end of block, Excepts on anything else
    def checkEnd(self, token):
        if token[1] == "end":
            token = self.scanner.nextToken()
            if token[1] == '.':
                return True
            else:
                return False

    # Since the end token is not an end. then check for the beginning of another program block
    def checkBeg(self, token):
        if token[1] == "begin":
            return True
        else:
            raise NameError('Expected begin keyword')


