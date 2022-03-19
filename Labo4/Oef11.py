def unique_characters(string):
    out = {}
    for i in string:
        out[i] = "aanwezig"
    return len(out)

print(unique_characters("Ik hou van Python!"))