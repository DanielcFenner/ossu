def f(x,y):
    x + y -2

# str2 = 'number one - the larch'
# str2 = str2.capitalize()
# str2.swapcase()
# print(str2)
# print(str2.index('n'))

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     if exp == 1:
#       return 1
#     else:
#       return base * iterPower(base, exp - 1)

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    for i in range(exp - 1):
        result = result * base
    return result
        

print(iterPower(9.84, 0))
print(iterPower(2,3))