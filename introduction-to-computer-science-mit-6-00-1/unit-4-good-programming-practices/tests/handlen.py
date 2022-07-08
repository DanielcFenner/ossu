def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for char in hand.keys():
        handLen += hand[char]
    return handLen

print(calculateHandlen({'a': 1, 'b': 1}))