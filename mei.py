import xml.etree.ElementTree as ET
import os

def get_all_notes():
    script_dir = os.path.dirname(__file__)
    file_path = raw_input('Please enter path to xml/mei file:\n')
    abs_file_path = os.path.join(script_dir, file_path)

    tree = ET.parse(abs_file_path)
    root = tree.getroot()

    sequence = ""
    notes = root.findall('.//{http://www.music-encoding.org/ns/mei}note')
    for note in notes:
        sequence += note.attrib['pname']
    return sequence
