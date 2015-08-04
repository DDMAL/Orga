import xml.etree.ElementTree as ET
import os
import sys

script_dir = os.path.dirname(__file__)
file_path = raw_input('Please enter path to xml/mei file:\n')
abs_file_path = os.path.join(script_dir, file_path)

tree = ET.parse(abs_file_path)
root = tree.getroot()

notes = root.findall('.//{http://www.music-encoding.org/ns/mei}note')
for note in notes:
    sys.stdout.write(note.attrib['pname'])
sys.stdout.flush()
print '\n'
