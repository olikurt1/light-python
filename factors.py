def Factors(n):
    factorList = []
    for x in range(1, n+1):
        if n % x == 0:
            factorList.append(x)

    return factorList

print(Factors(12))