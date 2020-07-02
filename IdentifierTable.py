id_table = []

class Identifier(object):
    value = ""
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value

class IdentifierTable(object):
    def lookup(self, obj):
        if obj in id_table:
            return True
        else:
            return False

    def store(self, obj):
        id_table.append(obj);

class PascalParser(object):
    pass
