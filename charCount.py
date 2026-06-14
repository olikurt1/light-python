def charCount(s):
    #in a dictionary, assigning to a key that doesn't exist creates the key at the same time as providing a value to its
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
    