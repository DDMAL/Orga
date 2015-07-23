sequence = raw_input("Enter Volpiano pitch sequence:\n")
print sequence
volpiano_map =  {'h':'a', 'j':'b', 'k':'c',
                 'l':'d', 'm':'e', 'n':'f',
                 'o':'g', 'p':'a', 'q':'b',
                 'r':'c', 's':'d', '9':'g'}

new_sequence = ""
for s in sequence:
    if s not in volpiano_map:
        new_sequence += s
    else:
        new_sequence += volpiano_map.get(s)

print new_sequence
