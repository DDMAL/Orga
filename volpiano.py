import csv
import os

# Queries csv file for volpiano pitches for a single side of Folio
def query():
    script_dir = os.path.dirname(__file__)
    file_path = raw_input('Enter path to csv file to be queried:\n')
    abs_file_path = os.path.join(script_dir, file_path)

    notes = ""

    with open(abs_file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        page = raw_input('Enter desired Folio number:\n')

        previous = None
        is_folio_found = False

        for row in reader:
            if row['Folio'] == page:
                is_folio_found = True
                if previous['Folio'] != page:
                    #print previous['Folio'], previous['Volpiano']
                    #print '\n'
                    notes += previous['Volpiano']
                #print row['Folio'], row['Volpiano']
                #print '\n'
                notes += row['Volpiano']
            else:
                if is_folio_found:
                    # print row['Folio'], row['Volpiano']
                    notes += row['Volpiano']
                    is_folio_found = False
            previous = row

        return notes

# Converts volpiano symbols to diatonic notes
def convert():
    sequence = raw_input("Enter Volpiano note sequence:\n")

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
def remove():
    sequence = raw_input("Enter sequence:\n")
    to_remove = raw_input("Enter symbols to remove:\n").split()

    new_sequence = ""
    for s in sequence:
        if s not in to_remove:
            new_sequence += s

    return new_sequence





