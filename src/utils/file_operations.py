'''Module for file operations: read, write.'''

from os.path import join
from .config import FILE_PATH

def write(filename: str, buffer: list) -> bool:
    '''Write given buffer to given file address and return bool

    Args:
        file_address: string representing the file address
        buffer: list of strings to be written on file
    Returns:
        bool: True on succession and False on failure to write
    '''
    file_address = join(FILE_PATH, filename)
    try:
        with open(file_address, 'w', encoding='utf-8') as file:
            file.writelines(buffer)
            file.close()
            return True
    except NotADirectoryError:
        return False

def read(filename: str) -> tuple:
    '''Read the file from given address and return tuple containing the result

    Args:
        file_address: name of the file to read
    Returns:
        tuple: First argument is a bool, telling wether 
        operation was succesfull, and second is a list
        containing the result (bool, [str])
    '''
    file_address = join(FILE_PATH, filename)
    try:
        with open(file_address, 'r', encoding='utf-8') as file:
            payload = file.readlines()
            file.close()
            return (True, payload)
    except FileNotFoundError:
        return (False, ['Error occurred while trying to read the file'])
