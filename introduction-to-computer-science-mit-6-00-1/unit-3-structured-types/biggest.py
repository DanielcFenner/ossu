animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = -1
    biggestKey = ''
    for key in aDict.keys():
        if len(aDict[key]) > biggest:
            biggestKey = key
    return biggestKey

print(biggest(animals))

