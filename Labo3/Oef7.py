
def is_integer(text):
    out = text.strip()
    if(len(out) > 0):
        if(out[0] == "+" or "-"):
            out = out[1:]
        if(out.isdigit()):
            return True
        else:
            return False
    else:
        return False

print(is_integer("  +26  "))