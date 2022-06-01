# Example input
s = 'azcbobobegghakl'

biggest = ""
tempString = ""
lastLetter = ""

for letter in s:

    if lastLetter == "" or ord(letter) >= ord(lastLetter):
        tempString += letter
        if len(tempString) > len(biggest):
            biggest = tempString
    elif ord(letter) < ord(lastLetter):
        tempString = letter

    lastLetter = letter

print("Longest substring in alphabetical order is: " + biggest)
