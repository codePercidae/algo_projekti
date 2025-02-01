from math import copysign, floor

class Converter:
    '''Class for turning abc-formatted files into list of integers
    and vice versa. Supports key-signatures up to 7 accidentals.'''

    def __init__(self):
        '''Create dictionaries for number/note relationships
        and key signatures'''

        self.notes_to_numbers = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        }

        self.numbers_to_notes = {
            0: 'C', 2: 'D', 4: 'E', 5: 'F',
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
        '''Reset the key~note relation and key back to original.'''

        self.key = 0
        self.notes_to_numbers = {
            'C': 0, 'D': 2, 'E': 4, 'F': 5,
            'G': 7, 'A': 9, 'B': 11, 'c': 12,
            'd': 14, 'e': 16, 'f': 17, 'g':19,
            'a': 21, 'b': 23
        }

    def apply_key(self, key: str) -> None:
        '''Mutate the note-number relation to match the key of the song

        Args:
            key: string representing the key of the song (Ex: C#m)
        Retuns:
            None
        '''
        self.reset()
        if key not in self.keys:
            raise ValueError('Malformatted key!')
        self.key = self.keys[key]
        accidentals = abs(self.keys[key])
        direction = 0
        if self.keys[key] > 0:
            note_to_change_i = 5
            note_to_change_c = 'F'
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

    def convert(self, file: list) -> list:
        '''Search for viable starting row in a file and
        pass it on to parse_row function, or apply
        the current key onto note~int relation

        Args: 
            file: contents of the file, saved in list row by row [str]
        Returns:
            Numerical representations of the notes, in a list
        '''
        converted_file = []
        for row in file:
            if row[0] in 'HIJLMNOPQRSTUWXZmrsw%':
                pass
            elif row[0] in 'CDEFGAHB' and row[1] == ":":
                pass
            elif row[0] == 'K':
                self.apply_key(row[2:].replace('\n', ''))
            else:
                converted_file.extend(self.parse_row(row.replace('\n', '')))
        return converted_file

    def parse_row(self, row: str) -> list:
        '''Filter unwanted symbols from the row and
        turn note names into numbers according the key
        and accidental markings.

        Args:
            row: a row of a file to be converted
        Returns:
            Numerical representations of the notes, in a list [int]
            If no viable symbol is found, returns empty list
        '''
        unallowed = ' /<>"1234567890.~HLMOPSTuvzZ/n}{`'
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


    def reverse_convert(self, generated_lists: list) -> None:
        '''Turn generated lists of integers into abc-format

        Args:
            generated_lists: lists of integers [[int]]
        Retuns:
            None
        '''
        #Edelleen ongelmia
        abc_formatted = []
        for song in generated_lists:
            row = '|'
            for i, n in enumerate(song):
                if n in self.numbers_to_notes:
                    row += self.numbers_to_notes[n]
                elif abs(n%24) in self.numbers_to_notes:
                    if n > 0:
                        sign = '`'
                    else:
                        sign = '_'
                    row += sign*floor(n/24) + self.numbers_to_notes[abs(n%24)]
                else:
                    row += '^' + self.numbers_to_notes[n-1]
                if i > 0 and (i+1) % 4 == 0:
                    row += '|'
            row += '\n\n'
            abc_formatted.append(row)
        return abc_formatted


    def chunk(self, values: list, degree: int) -> list:
        '''Chop the converted list into sublists for training the trie

        Args:
            values: converted file as list of integers
            degree: tells how long chopped lists are
        Returns:
            sublists of values in a list [[int]]
        '''
        ret = []
        for i in range(len(values) - degree):
            ret.append(values[i:i+degree])
        return ret
