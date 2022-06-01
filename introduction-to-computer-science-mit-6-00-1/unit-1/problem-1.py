# Example input
s = 'azcbobobegghakl'

vowels = "aeiou"
count = 0

for letter in s:
    if letter in vowels:
        count += 1

print(count)