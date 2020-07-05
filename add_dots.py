def add_dots(string):
    '''
    Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
    '''
    dot = "."
    result = ""
    lst = list(string)
   
    result = dot.join(lst)
    return result

       
        
def remove_dots(string):
    result = ""
    # result = string.replace(".", "")  #another way to do it
    for i in range(len(string)):
        if string[i] == ".":
            continue
        result += string[i]
    return result       


# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")


print(remove_dots("h.ee.l.l.o.oo."))

print(remove_dots(add_dots("test")))