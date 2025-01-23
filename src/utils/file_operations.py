

def write(file_address: str, buffer: list) -> bool:
    '''Writes given buffer to given file address
    Args:
        file_address: string representing the file address
        buffer: list of strings to be written on file
    Returns:
        bool: True on succession and False on failure to write
    '''
    try:
        file = open(file_address, 'w')
        for string in buffer:
            file.write(string)
        file.close()
        return True
    except:
        return False

def read(file_address: str) -> tuple:
    '''Reads the file from given address
    Args:
        file_address: name of the file to read
    Returns:
        tuple: First argument is a bool, telling wether 
        operation was succesfull, and second is a list
        containing the result
    '''
    payload = []
    try:
        file = open(file_address)
        for row in file:
            payload.append(row)
        file.close()
        return (True, payload)
    except:
        return (False, ['Error occurred while trying to read the file'])