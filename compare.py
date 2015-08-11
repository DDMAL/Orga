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

mei_files = os.listdir(MEI_PATH)

for mei_file in mei_files:
    if mei_file in (".DS_Store", "Icon\r"):
        continue

    # Queries for Volpiano notes in corresponding mei_file
    folio = os.path.splitext(mei_file)[0]
    queried_notes = volpiano.query(CSV_PATH + CSV_FILE, folio)
    converted_notes = volpiano.convert(queried_notes)

    symbols = ['1', '3', '7','4','-', 'i',
               '5', '6','2','I', 'w', 'W',
               'x', 'X', 'y','Y', 'z', 'Z']

    volpiano_notes = volpiano.remove(converted_notes, symbols)

    # Queries for all mei notes in mei_file
    mei_notes = mei.get_all_notes(MEI_PATH + mei_file)

    # Outputs file containing notes to compare and relevant meta data
    with open("../results/COMPARE/" + folio + "_compare.txt", "w") as fo:
        fo.write(str(dt) + "\n")
        fo.write("\n" + "mei_notes in " + mei_file + "\n")
        fo.write(notes.count(mei_notes) + "\n")
        fo.write("\n" + mei_notes + "\n")
        fo.write("\n" + "volpiano_notes from " + CSV_FILE + " in folio: " + folio + "\n")
        fo.write(notes.count(volpiano_notes) + "\n")
        fo.write("\n" + volpiano_notes + "\n")
