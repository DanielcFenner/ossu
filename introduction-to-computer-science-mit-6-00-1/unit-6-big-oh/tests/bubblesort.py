import random

def bubbleSort(list):
    swap = False
    while not swap:
        swap = True
        for i in (range(1, len(list))):
            if list[i] < list[i-1]:
                swap = False
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
    return list

randomList = []
for i in range(5000):
    randomList.append(random.random() * 100)

print(bubbleSort(randomList))
