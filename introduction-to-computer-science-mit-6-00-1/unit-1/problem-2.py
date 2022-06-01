# Example input
s = 'azcbobobegghakl'

count = 0
bob = 'bob'

for i in range(0, (len(s) + 1) - len(bob)):
    if s[i] + s[i+1] + s[i+2] == bob:
        count += 1

print(count)
