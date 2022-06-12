def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i in reversed(range(a + 1)):
        if a % i == 0 and b % i == 0:
            return i

print(gcdIter(2, 12))
print(gcdIter(6, 12))
