import csv
import os

script_dir = os.path.dirname(__file__)
file_path = raw_input('Enter path to csv file to be queried:\n')
abs_file_path = os.path.join(script_dir, file_path)

with open(abs_file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    page = raw_input('Enter desired Folio number:\n')

    previous = None
    is_folio_found = False

    for row in reader:
        if row['Folio'] == page:
            is_folio_found = True
            if previous['Folio'] != page:
                print previous['Folio'], previous['Volpiano']
                print '\n'
            print row['Folio'], row['Volpiano']
            print '\n'
        else:
            if is_folio_found:
                print row['Folio'], row['Volpiano']
                is_folio_found = False
        previous = row
