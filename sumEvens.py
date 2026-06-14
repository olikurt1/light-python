def sumEvens(L):
    total = 0
    for num in L:
        if num % 2 == 0:
            total += num
    return total