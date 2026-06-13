#to check if a number is prime have to check that its not divisible by a number thats not itself or 1
def isPrime(num):
    if num < 2:
        return False
    else:
        #loops through every possible operation 
        for x in range(2, num):
            #as soon as selection is met its known that there is a divisor between itself and 2 so not prime
            if num % x == 0:
                return False
        #if selection with return false isn't triggered that means by default the number is prime
        return True

