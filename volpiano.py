import csv
import os

# Queries csv file for volpiano pitches for a single side of Folio
def query(file_path, folio, debug=False):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_path)

    notes = ""

    with open(abs_file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        page = folio

        previous = None
        is_folio_found = False

        for row in reader:
            if row['Folio'] == page:
                is_folio_found = True
                if previous is not None and previous['Folio'] != page:

                    if debug:
                        print previous['Folio'], previous['Volpiano']
                        print '\n'

                    notes += previous['Volpiano']

                if debug:
                    print row['Folio'], row['Volpiano']
                    print '\n'
                    
                notes += row['Volpiano']
            else:
                if is_folio_found:

                    if debug:
                        print row['Folio'], row['Volpiano']

                    notes += row['Volpiano']
                    is_folio_found = False
            previous = row

        return notes

# Converts volpiano symbols to diatonic notes
def convert(sequence):

    volpiano_map =  {'h':'a', 'j':'b', 'k':'c',
                    'l':'d', 'm':'e', 'n':'f',
                    'o':'g', 'p':'a', 'q':'b',
                    'r':'c', 's':'d', '9':'g'}

    new_sequence = ""
    for s in sequence:
        if s not in volpiano_map:
            new_sequence += s
        else:
            new_sequence += volpiano_map.get(s)

    return new_sequence

# Removes desired symbols from input sequence
def remove(sequence, symbols):
    to_remove = symbols

    new_sequence = ""
    for s in sequence:
        if s not in to_remove:
            new_sequence += s

    return new_sequence





