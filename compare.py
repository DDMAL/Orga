import volpiano
import mei
import note
from datetime import datetime


csvfile = "sal-data.csv"
Folio = "003r"
notes = volpiano.query("../data/" + csvfile, Folio)
converted_notes = volpiano.convert(notes)
symbols = ['1', '3', '7', '4', '-', 'i']
extracted_notes = volpiano.remove(converted_notes, symbols)

mei_file = "CF-010.xml"
mei_notes = mei.get_all_notes("../data/" + mei_file)

dt = datetime.now()
dt = dt.replace(second=0, microsecond=0)

with open("test.txt", "w") as fo:
    fo.write(str(dt) + "\n")
    fo.write("\n" + "mei_notes from " + mei_file + "\n")
    fo.write("\n" + mei_notes + "\n")
    fo.write("\n" + "volpiano_notes from " + csvfile + " in Folio: " + Folio + "\n")
    fo.write("\n" + extracted_notes + "\n")
