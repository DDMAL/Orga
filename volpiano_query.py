import csv
import os

script_dir = os.path.dirname(__file__)
file_path = raw_input('Enter path to csv file to be queried:\n')
abs_file_path = os.path.join(script_dir, file_path)
with open(abs_file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    page = raw_input('Enter desired Folio number:\n')
    for row in reader:
        if row['Folio'] == page:
            print row['Volpiano']
            print '\n'


