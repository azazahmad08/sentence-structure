# Find Sentence total Letter Digit And Word;

numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0

text = input("Enter your sentence here :")
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberOfLetters = numberOfLetters + 1
    elif x >= '0' and x <= '9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 2
print("Total Number of Letters is:",numberOfLetters)
print("Total Number of Digit is:",numberOfDigits)
print("Total Number of Word is:",numberOfWords)
