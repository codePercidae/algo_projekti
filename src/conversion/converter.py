from math import copysign
from utils import file_operations

class Converter:
    def __init__(self):
        '''Creates a dictionary for number/note relationship'''
        self.notes_to_numbers = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        }

        self.numbers_to_notes = {
            0: 'C', 2: 'D', 4: 'E', 'F': 5,
            7: 'G', 9: 'A', 11: 'B', 12: 'c',
            14: 'd', 16: 'e', 17: 'f', 19: 'g',
            21: 'a', 23: 'b' 
        }

        self.keys = {
            'C': 0, 'G': 1, 'D': 2, 'A': 3, 'E': 4, 'B': 5,
            'F#': 6, 'C#': 7, 'F': -1, 'Bb': -2, 'Eb': -3,
            'Ab': -4, 'Db': -5, 'Gb': -6, 'Cb': -7, 'Am': 0,
            'Em': 1, 'Hm': 2, 'F#m': 3, 'C#m': 4, 'G#m': 5, 
            'D#m': 6, 'A#m': 7, 'Dm': -1, 'Gm': -2, 'Cm': -3, 
            'Fm': -4, 'Bbm': -5, 'Ebm': -6, 'Abm': -7
        }

        self.key = 0

    def reset(self):
        self.key = 0
        self.notes_to_numbers = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        }

    def apply_key(self, key: str) -> None:
        '''Mutates the note-number relation to match
        the key of the song
        Args:
            key: string representing the key of the song
        Retuns:
            None
        '''
        self.reset()
        if key not in self.keys:
            raise ValueError('Malformatted key!')
        self.key = self.keys[key]
        accidentals = abs(self.keys[key])
        if self.keys[key] > 0:
            note_to_change_i = 5
            note_to_change_c = 'G'
            direction = 1
        elif self.keys[key] < 0:
            note_to_change_i = 11
            note_to_change_c = 'B'
            direction = -1
        elif self.keys[key] == 0:
            return
        for i in range(accidentals):
            self.notes_to_numbers[note_to_change_c] += direction
            self.notes_to_numbers[note_to_change_c.lower()] += direction
            note_to_change_i = (note_to_change_i + (7*direction)) % 12
            note_to_change_c = self.numbers_to_notes[note_to_change_i]
        return 

    def convert(self, filename: str) -> list:
        '''Searches for viable starting row in a file and
        passes it on to parse_row function, or applies
        the current key onto note~int relation
        Args: 
            filename: Name of the file to be converted
        Returns:
            Numerical representations of the notes, in a list
        '''
        converted_file = []
        file = open(filename)
        for row in file:
            if row[0] in 'HIJLMNOPQRSTUWXZmrsw%':
                pass
            elif row[0] in 'CDEFGAHB' and row[1] == ":":
                pass
            elif row[0] == 'K':
                self.apply_key(row[2:].replace('\n', ''))
            else:
                converted_file.extend(self.parse_row(row.replace('\n', '')))
        file.close()
        return converted_file

    def parse_row(self, row: str) -> list:
        '''Filters unwanted symbols from the row and
        turns note names into numbers accoring the key
        and accidental markings
        Args:
            row: a row of a file to be converted
        Returns:
            Numerical representations of the notes, in a list [int]
            If no viable symbol is found, returns empty list
        '''
        unallowed = ' /<>"1234567890.~HLMOPSTuvzZ/n'
        note_numbers = []
        returned_notes = {}
        performance_marking = False
        next_note_returned = False
        chord_marking = False
        sharp, flat = 0, 0
        for c in row:
            if c == '!':
                performance_marking = not performance_marking
            elif c == '(':
                chord_marking = True
            elif c == ')':
                chord_marking = False 
            elif performance_marking or chord_marking or c in unallowed:
                pass
            elif len(returned_notes) > 0 and c in '|[]:':
                returned_notes = {}
            elif c in '|[]:':
                pass
            elif c in returned_notes:
                note_numbers.append(returned_notes[c])
            elif next_note_returned:
                returned_notes[c] = self.notes_to_numbers[c] + copysign(1, self.key)
                note_numbers.append(returned_notes[c])
                next_note_returned = False
            elif c in 'cdefgabCDEFGAB':
                note_numbers.append(self.notes_to_numbers[c]+sharp+flat)
                sharp, flat = 0, 0
            elif c == '=':
                next_note_returned = True
            elif c == '^':
                sharp += 1
            elif c == '_':
                flat -= 1
            elif c == "'":
                note_numbers.append(note_numbers.pop() + 12)
            elif c == ',':
                note_numbers.append(note_numbers.pop() - 12)
            else:
                err_msg = f'Failure to identify a character: "{c}"'
                raise ValueError(err_msg)
        return note_numbers


    def reverse_converter(self, generated_lists: list) -> None:
        '''Turns generated list of integers into abc-format and
        passes it to file operations for writing. 
        Args:
            generated_lists: lists of integers [[int]]
        Retuns:
            None
        '''
        #Edelleen ongelmia
        buffer = []
        for song in generated_lists:
            row = '|'
            for i in song:
                if i in self.numbers_to_notes:
                    row += self.numbers_to_notes[i]
                else:
                    row += '^' + self.numbers_to_notes[i-1]
                    pass
            row += '|\n\n'
            buffer.append(row)
        file_operations.write('music.txt', buffer)


    def chunk(self, values: list) -> list:
        '''Chops the converted list into sublists for training the trie
        Args:
            values: converted file as list of integers
        Returns:
            all sublists of values in a list
        '''
        ret = []
        for i in range(len(values)):
            for j in range(len(values)):
                new = values[i:j+1]
                if new:
                    ret.append(new)
        return ret