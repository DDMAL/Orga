import volpiano
import mei
import notes
import os
import emboss
from datetime import datetime

dt = datetime.now()

DATA_PATH = "../data/"
CSV_PATH = "../data/csv_files/"
CSV_FILE = "sal-data.csv"
MEI_PATH = "../data/mei_files/"
RESULT_PATH = "../results/EMBOSS/"

VOLPIANO_SYMBOLS = ['1', '3', '7', '4', '-', 'i',
                    '5', '6', '2', 'I', 'w', 'W',
                    'x', 'X', 'y', 'Y', 'z', '']

VOLPIANO_MAP = {'h':'a', 'j':'b', 'k':'c',
                'l':'d', 'm':'e', 'n':'f',
                'o':'g', 'p':'a', 'q':'b',
                'r':'c', 's':'d', '9':'g'}

mei_files = os.listdir(MEI_PATH)

for mei_file in mei_files:
    if mei_file in (".DS_Store", "Icon\r"):
        continue

    # Queries for Volpiano notes in corresponding mei_file
    folio = os.path.splitext(mei_file)[0]
    queried_notes = volpiano.query(os.path.join(CSV_PATH, CSV_FILE), folio)[0]
    converted_notes = notes.convert(queried_notes, VOLPIANO_MAP)
    volpiano_notes = notes.remove(converted_notes, VOLPIANO_SYMBOLS)

    # Obtains the folio numbers for the next and previous chant with respect to the queried folio.
    previous_chant = volpiano.query(os.path.join(CSV_PATH, CSV_FILE), folio)[1]
    next_chant = volpiano.query(os.path.join(CSV_PATH, CSV_FILE), folio)[2]

    # Queries for all mei notes in mei_file
    mei_notes = mei.get_all_notes(MEI_PATH + mei_file)

    # Sequence alignment the mei notes and volpiano notes
    gapopen = 10
    gapextend = 0.5
    matrix = 'EBLOSUM62'

    outfile1 = os.path.join(RESULT_PATH, folio + '_local.txt')
    emboss.needle(mei_notes, volpiano_notes, gapopen, gapextend, matrix, outfile1)

    outfile2 = os.path.join(RESULT_PATH, folio + '_global.txt')
    emboss.water(mei_notes, volpiano_notes, gapopen, gapextend, matrix, outfile2)

    outfiles = [outfile1, outfile2]

    # Appends meta data to file containing alignment information
    for outfile in outfiles:
        with open(outfile, "a") as fo:
            fo.write(str(dt) + "\n")
            fo.write("\n" + "mei_notes in " + mei_file + "\n")
            fo.write(notes.count(mei_notes) + "\n")
            fo.write("\n" + mei_notes + "\n")
            fo.write("\n" + "volpiano_notes from " + CSV_FILE + " in folio: " + folio)
            fo.write(" (previous_chant: " + previous_chant + ", next_chant: " + next_chant + ") ")
            fo.write("\n" + notes.count(volpiano_notes) + "\n")
            fo.write("\n" + volpiano_notes + "\n")


