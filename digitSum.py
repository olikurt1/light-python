def digitSum(n):
    sepNums =[]
    while n > 0:
        digit = n % 10
        n = n //10
        sepNums.append(digit)
    sum = 0
    for dig in sepNums:
        sum += dig
    return sum
 

print(digitSum(99))


