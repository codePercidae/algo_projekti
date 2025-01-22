def write(file_address: str, buffer: list) -> bool:
    '''Writes given buffer to given file address
    Args:
        file_address: string representing the file address
        buffer: string to be written on file
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

def read(file_address: str) -> str:
    file = open(file_address,)
    payload = file.read()
    file.close()
    return payload