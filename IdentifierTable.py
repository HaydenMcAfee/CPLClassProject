class Identifier(object):
    value = ""
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value

class IdentifierTable(object):
    id_table = []

    def lookup(self, obj):
        if obj in self.id_table:
            return True
        else:
            return False

    def store(self, obj):
        self.id_table.append(obj);

    def getAll(self):
        print(*self.id_table, sep = "\n")


class PascalParser(object):
    pass
