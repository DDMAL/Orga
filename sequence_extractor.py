sequence = raw_input("Enter sequence:\n")
to_remove = raw_input("Enter symbols to remove:\n").split()

new_sequence = ""
for s in sequence:
    while s not in to_remove:
        new_sequence += s
        break

print new_sequence
