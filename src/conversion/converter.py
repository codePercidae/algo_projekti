class Converter:
    def __init__(self):
        #täytyy ottaa huomioon oktaavit?
        self.notes = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'H': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'h': 23
        }

    #convert searches for viable starting row from abc-file
    #and when finds one, passes it on parser. Converter returns
    #list with integers representing the notes.
    def convert(self, filename: str) -> list:
        converted_file = []
        file = open(filename)
        for row in file:
            if row[0] in 'HIJKLMNOPQRSTUWXZmrsw%':
                pass
            elif row[0] in 'CDEFGAHB' and row[1] == ":":
                pass
            else:
                converted_file.extend(self.parse_row(row))
        file.close()
        return converted_file

    def parse_row(self, row):
        unallowed = ' /|[]:<>"1234567890.~HLMOPSTuvzZ'
        note_numbers = []
        performance_marking = False
        sharp, flat = 0, 0
        for c in row:
            if c == '!':
                performance_marking = not performance_marking
            elif performance_marking or c in unallowed:
                pass
            elif c == '=':
                pass
                #miten palautus hoidetaan???
            elif c == '^':
                sharp += 1
            elif c == '_':
                flat -= 1
            elif c in 'cdefgabCDEFGHAB':
                note_numbers.append(self.notes[c]+sharp+flat)
                sharp, flat = 0, 0
            else:
                err_msg = f'Failure to identify a character: {c}'
                raise ValueError(err_msg)
        return note_numbers




