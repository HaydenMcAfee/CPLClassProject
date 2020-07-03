# CS 4308
# W01
# Language Processor Deliverable 2
# 7-2-20
# Kaden Llewellyn and Hayden McAfee
# etc.

# The identifier object has a value attribute to store its value
class Identifier(object):
    value = ""
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value

# The identifier table holds many identifiers and can be checked and stored to
class IdentifierTable(object):
    id_table = []

    # Returns true if identifier is in table, false if not
    def lookup(self, obj):
        if obj in self.id_table:
            return True
        else:
            return False

    # Stores identifier in table
    def store(self, obj):
        self.id_table.append(obj);

    # Returns all of the stored identifiers from the table
    def getAll(self):
        print(*self.id_table, sep = "\n")
