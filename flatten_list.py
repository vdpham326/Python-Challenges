def flatten (l):
    '''
    Write a function that takes a list of lists and flattens it into a one-dimensional list.
    '''
    result = []

    for i in l:
        for j in i:
            result.append(j)
    return result

# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]