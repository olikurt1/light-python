def reverseNum(n):
    result = 0
    while n > 0:  
        digit = n % 10
        n = n // 10 
        result = result*10 + digit
    return result
