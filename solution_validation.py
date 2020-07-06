def validate(s):
    if "def" not in s:
        return "missing def"
    if ":" not in s:
        return "missing :"
    if "(" and ")" not in s:
        return "missing paren"
    if "(" + ")" in s:
        return "missing param"
    if "    " not in s:
        return "missing indent"
    if "validate" not in s:
        return "wrong name"
    if "return" not in s:
        return "missing return"
    return True


# another solution
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

#another using dictionary
def validate(string):
    dos = {
        "def":"missing def",
        ":":"missing :",
        "(":"missing paren",
        ")":"missing paren",
        "    ":"missing indent",
        "validate":"wrong name",
        "return":"missing return"
    }

    donts = {"()":"missing param"}

    for key in dos:
        if key not in string:
            print(dos[key])
            return dos[key]

    for key in donts:
        if key in string:
            print (donts[key])
            return donts[key]
    return True