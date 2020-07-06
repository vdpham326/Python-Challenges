def list_xor(n, list1, list2):
    '''
    Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
    Your function must return whether n is exclusively in list1 or list2.
    In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.
    '''
    return (n in list1 and n not in list2) or (n in list2 and n not in list1)


# smart solution: uses the built-in xor operator ^
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)

# naive solution: check each case at a time
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True

    