class Converter:
    def __init__(self):
        '''Creates a dictionary for number/note relationship'''
        #täytyy ottaa huomioon oktaavit? Paremmin?
        self.notes = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        }

    def convert(self, filename: str) -> list:
        '''Searches for viable starting row in a file and
        passes it on to parse_row function
        Args: 
            filename: Name of the file to be converted
        Returns:
            Numerical representations of the notes, in a list [int]
            If no viable row is found, returns empty list
        '''
        #sävellaji????
        converted_file = []
        file = open(filename)
        for row in file:
            if row[0] in 'HIJKLMNOPQRSTUWXZmrsw%':
                pass
            elif row[0] in 'CDEFGAHB' and row[1] == ":":
                pass
            else:
                converted_file.extend(self.parse_row(row.replace('\n', '')))
        file.close()
        return converted_file

    def parse_row(self, row):
        '''Filters unwanted symbols from the row and
        turns note names into numbers
        Args:
            row: a row of a file to be converted
        Returns:
            Numerical representations of the notes, in a list [int]
            If no viable symbol is found, returns empty list
        '''
        unallowed = ' /|[]:<>"1234567890.~HLMOPSTuvzZ/n'
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
                err_msg = f'Failure to identify a character: "{c}"'
                raise ValueError(err_msg)
        return note_numbers


# täytyy olla myös käänteinen konvertteri? from int to txt

