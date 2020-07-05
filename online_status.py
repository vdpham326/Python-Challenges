def online_count(dictionary):
    """
    Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline".
    Your function should return the number of people who are online.
    """
    count = 0
    for key in dictionary:
        if dictionary[key] == 'online':
            count += 1
    return count

# alt version
def online_count(dictionary):
    """
    Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline".
    Your function should return the number of people who are online.
    """
    count = 0
    for val in dictionary.values():
        if val == 'online':
            count += 1
    return count


# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])