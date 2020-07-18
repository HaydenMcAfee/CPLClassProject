# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

# The identifier object has a value attribute to store its value
class Identifier(object):
    name = ""
    value = ""
    type = ""
    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

# The identifier table holds many identifiers and can be checked and stored to
class IdentifierTable(object):
    idTable = []

    # Returns true if identifier is in table, false if not
    def lookup(self, name):
        temp = Identifier()
        for id in self.idTable:
            temp = id
            if temp.getName() == name:
                return True
        return False


    # Stores identifier in table
    def store(self, ident):
        temp = Identifier()
        temp.setName(ident)
        if len(self.idTable) == 0:
            self.idTable.append(temp)
        else:
           self.idTable.append(temp)

    def storeVal(self, name, val, type):
        temp = Identifier()
        for id in self.idTable:
            temp = id
            if temp.getName() == name:
                temp.setValue(val)
                temp.setType(type)
                id = temp
                
    def getVal(self, name):
        temp = Identifier()
        for id in self.idTable:
            temp = id
            if temp.getName() == name:
                return temp.getValue()

    def getType(self, name):
        temp = Identifier()
        for id in self.idTable:
            temp = id
            if temp.getName() == name:
                return temp.getType()


    # Returns all of the stored identifiers from the table
    def getAll(self):
        temp = Identifier()
        for id in self.idTable:
            temp = id
            print(str(temp.getName()) + " = " + str(temp.getValue()))

# Method tests
# def __main__():
#
#     idTable = IdentifierTable()
#
#     idTable.store("hello")
#     print(idTable.lookup("hello"))
#     idTable.storeVal("hello",1)
#     idTable.getAll()
#     print(idTable.getVal("hello"))
#
# __main__()