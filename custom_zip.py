def zap(a, b):
    '''
    Define a function named zap. The function takes two parameters, a and b. These are lists.
    Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
    You may assume a and b have equal lengths.
    '''
    result = []
    
    for i in range(len(a)):
        val_a = a[i]
        val_b = b[i]
        final_tup = (val_a, val_b) # create a tuple with the elementfrom a and b
        result.append(final_tup)

    return result


# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result

# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]


print(zap([1, 2], [3, 4]))