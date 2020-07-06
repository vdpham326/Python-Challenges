def largest_difference(l):
    '''
    Define a function named largest_difference that takes a list of numbers as its only parameter.
    Your function should compute and return the difference between the largest and smallest number in the list.
    '''
    # largest = smallest = l[0]

    # for index in range(1, len(l)):
    #     if l[index] > largest:
    #         largest = l[index]
    #     if l[index] < smallest:
    #         smallest = l[index]

    largest = max(l)
    smallest = min(l)
    return largest - smallest


# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference


print(largest_difference([1, 2, 90]))

