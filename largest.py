def largest(L):
    #L[0] means it includes a real member as opposed to just returning 0 even though a negative number may truly be the biggest value
    largest = L[0]
    for num in L:
        if num > largest:
            largest = num

    return largest