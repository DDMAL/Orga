import volpiano
import mei
import note
import os
from datetime import datetime

dt = datetime.now()

CSV_FILE = "sal-data.csv"
DATA_PATH = "../data/"
MEI_PATH = "../data/mei_files/"

mei_files = os.listdir(MEI_PATH)

for mei_file in mei_files:
    if mei_file in (".DS_Store", "Icon?"):
        continue

    # Queries for Volpiano notes in corresponding mei_file
    folio = os.path.splitext(mei_file)[0]
    notes = volpiano.query(DATA_PATH + CSV_FILE, folio)
    converted_notes = volpiano.convert(notes)

    symbols = ['1', '3', '7','4','-', 'i',
               '5', '6','2','I', 'w', 'W',
               'x', 'X', 'y','Y', 'z', 'Z']

    extracted_notes = volpiano.remove(converted_notes, symbols)

    # Queries for all mei notes in mei_file
    mei_notes = mei.get_all_notes(MEI_PATH + mei_file)

    # Outputs file containing notes to compare and relevant meta data
    with open("../tests/" + folio + "_compare.txt", "w") as fo:
        fo.write(str(dt) + "\n")
        fo.write("\n" + "mei_notes in " + mei_file + "\n")
        fo.write(note.count(mei_notes) + "\n")
        fo.write("\n" + mei_notes + "\n")
        fo.write("\n" + "volpiano_notes from " + CSV_FILE + " in folio: " + folio + "\n")
        fo.write(note.count(extracted_notes) + "\n")
        fo.write("\n" + extracted_notes + "\n")
