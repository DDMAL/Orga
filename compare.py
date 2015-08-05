import volpiano
import mei
import note
from datetime import datetime


csvfile = "sal-data.csv"
folio = "003r"
notes = volpiano.query("../data/" + csvfile, folio)
converted_notes = volpiano.convert(notes)
symbols = ['1', '3', '7', '4', '-', 'i']
extracted_notes = volpiano.remove(converted_notes, symbols)

mei_file = "CF-010.mei"
mei_notes = mei.get_all_notes("../data/" + mei_file)

dt = datetime.now()

with open("../tests/trial.txt", "w") as fo:
    fo.write(str(dt) + "\n")
    fo.write("\n" + "mei_notes in " + mei_file + "\n")
    fo.write(note.count(mei_notes) + "\n")
    fo.write("\n" + mei_notes + "\n")
    fo.write("\n" + "volpiano_notes from " + csvfile + " in folio: " + folio + "\n")
    fo.write(note.count(extracted_notes) + "\n")
    fo.write("\n" + extracted_notes + "\n")
