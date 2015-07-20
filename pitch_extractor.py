String = raw_input("Enter vol-piano sequence:\n")

pitches = ""
for s in String:
    if s != "," and  s != "-":
        pitches += s

print pitches


