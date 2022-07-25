import random

# the worst sorting algorithm ever
def monkeySort(list):
    attempts = 0
    while not isSorted(list):
        attempts += 1
        print(attempts)
        random.shuffle(list)

def isSorted(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False      
    return True



# generate and test a random list
randomList = []
for i in range(15):
    randomList.append(random.random() * 100)
monkeySort(randomList)