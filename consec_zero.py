def consecutive_zeros(string):
    '''
    Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. 
    Your function should return the number described above.
    '''
    count = 0 # keep track of consecutive zeroes
    max_zero_count = 0 #keep track of the highest number of consecutive zero
    for i in string:
        if i == "0":
            count += 1
            if count > max_zero_count:
                max_zero_count = count
        if i == "1":
            count = 0

    return max_zero_count

# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])


print(consecutive_zeros("101"))