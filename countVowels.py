def CountVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    vowelCount = 0
    for l in s:
        if l.lower() in vowels:
            vowelCount += 1
    return vowelCount

print(CountVowels("pythOn"))