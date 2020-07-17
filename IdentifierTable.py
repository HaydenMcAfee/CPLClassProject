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
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value

# The identifier table holds many identifiers and can be checked and stored to
class IdentifierTable(object):
    id_table = Identifier[100]

    # Todo: I need this to return true if the name exists, only takes in a string
    # Returns true if identifier is in table, false if not
    def lookup(self, name):
        for id in self.id_table:
            if self.id_table[id] == name:
                return True
            else: return False


    # Todo: I need this to store the name of the identifier in the table at a the end index
    # Stores identifier in table
    def store(self, ident):
        for id in self.id_table:
            if self.id_table[id] == ident:
                self.id_table[5].set

    # Todo: I need a method to modify the indentifier by finding it with its name and setting that Identifier objects value field

    # Returns all of the stored identifiers from the table
    def getAll(self):
        print(*self.id_table, sep = "\n")
