import math


# find every subset/permutation of integers in list
def genSubsets(L):
	res = []
	if len(L) == 0:
		return [[]]
	smaller = genSubsets(L[:-1])
	extra = L[-1:]
	new = []
	for small in smaller:
		new.append(small+extra)
	return smaller+new

#find best combo of coin combinations with given target
def findBestCombo(list, target):
    coins = []
    for coin in list:
        coinAmount = math.ceil(target / coin)
        for i in range(coinAmount):
            coins.append(coin)
    combos = genSubsets(coins)
    bestCombo = []
    combosLength = len(combos)
    for combo in combos:
        print(combosLength)
        combosLength-=1
        if bestCombo == [] and (sum(combo) - target) >= 0:
            bestCombo = combo
        elif (sum(combo) - target) < (sum(bestCombo) - target) and (sum(combo) - target) >= 0:
            bestCombo = combo   
    return bestCombo
        

print(findBestCombo([0.92, 1.30, 2.71], 7))
