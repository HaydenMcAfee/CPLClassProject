from plex import *

class PascalScanner(object):
    def doScanner(self, lexicon, f, filename):
        scanner = Scanner(lexicon, f, filename)
        while 1:
            token = scanner.read()
            # The .read() function will return a tuple with the token and string and then their line and start column will be concatened to the output
            if token[0] is None:
                break
            print( str(token) + ": line: " + str(scanner.cur_line) + " col: " + str(scanner.start_col))
