def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    middle_aStr = int(len(aStr) / 2)

    if int(len(aStr)) == 0:
        return False
    elif int(len(aStr) == 1) and aStr[0] != char:
        return False
    elif char == aStr[middle_aStr]:
        return True
    elif char > aStr[middle_aStr]:
        return isIn(char, aStr[middle_aStr:])
    else:
        return isIn(char, aStr[0:middle_aStr])


testString = "abcdefghijklmnopqrstuvwxyz"
print(isIn('d', 'cejmuvz'))
