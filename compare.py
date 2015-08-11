import volpiano
import mei
import notes
import os
from datetime import datetime

dt = datetime.now()

DATA_PATH = "../data/"
CSV_PATH = "../data/csv_files/"
CSV_FILE = "sal-data.csv"
MEI_PATH = "../data/mei_files/"

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

    # Queries for all mei notes in mei_file
    mei_notes = mei.get_all_notes(MEI_PATH + mei_file)

    # Outputs file containing notes to compare and relevant meta data
    previous_chant = volpiano.query(os.path.join(CSV_PATH, CSV_FILE), folio)[1]
    next_chant = volpiano.query(os.path.join(CSV_PATH, CSV_FILE), folio)[2]

    with open("../results/COMPARE/" + folio + "_compare.txt", "w") as fo:
        fo.write(str(dt) + "\n")
        fo.write("\n" + "mei_notes in " + mei_file + "\n")
        fo.write(notes.count(mei_notes) + "\n")
        fo.write("\n" + mei_notes + "\n")
        fo.write("\n" + "volpiano_notes from " + CSV_FILE + " in folio: " + folio)
        fo.write(" (previous_chant: " + previous_chant + ", next_chant: " + next_chant + ") ")
        fo.write("\n" + notes.count(volpiano_notes) + "\n")
        fo.write("\n" + volpiano_notes + "\n")
