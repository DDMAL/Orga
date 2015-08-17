

def count(sequence):
    """Counts the the number of characters in sequence.

    Args:
        sequence (str): Input sequence.

    Returns:
        Number of characters in input sequence.

    """
    return "number of notes: {}".format(len(sequence))

def convert(sequence, map):
    """Maps characters in sequence to desired character.

    Args:
        sequence (str): Input sequence.
        map (dict): Dictionary of characters mapping to another character.

    Returns:
        Sequence with characters mapped to new characters according to input dictionary.

    """
    new_sequence = ""
    for s in sequence:
        if s not in map:
            new_sequence += s
        else:
            new_sequence += map.get(s)

    return new_sequence

def remove(sequence, symbols):
    """Removes desired symbols from input sequence.

    Args:
        sequence (str): Input sequence.
        symbols (list): List of symbols that is to be removed from input sequence.

    Returns:
        Sequence without characters in list of symbols.

    """
    to_remove = symbols

    new_sequence = ""
    for s in sequence:
        if s not in to_remove:
            new_sequence += s

    return new_sequence


