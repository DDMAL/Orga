import xml.etree.ElementTree as ET
import os

def get_all_notes(file_path):
	"""Extracts all values assigned to pname attribute of neume ElementTree.

	Args:
		file_path (str): Path to file from which elements will be extracted.

	"""
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_path)

    tree = ET.parse(abs_file_path)
    root = tree.getroot()

    sequence = ""
    notes = root.findall('.//{http://www.music-encoding.org/ns/mei}note')
    for note in notes:
        sequence += note.attrib['pname']
    return sequence

