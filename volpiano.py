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
        previous_chant = None
        next_chant = None

        for row in reader:
            if row['Folio'] == page:
                is_folio_found = True
                if previous is not None and previous['Folio'] != page:

                    if debug:
                        print previous['Folio'], previous['Volpiano']
                        print '\n'

                    global previous_chant
                    previous_chant = previous['Folio']
                    notes += previous['Volpiano']

                if debug:
                    print row['Folio'], row['Volpiano']
                    print '\n'

                notes += row['Volpiano']
            else:
                if is_folio_found:

                    if debug:
                        print row['Folio'], row['Volpiano']

                    global next_chant
                    next_chant = row['Folio']
                    notes += row['Volpiano']
                    is_folio_found = False

            previous = row

        if previous_chant is None:
            return (notes, "None", next_chant)
        elif next_chant is None:
            return (notes, previous_chant, "None")
        else:
            return (notes, previous_chant, next_chant)
