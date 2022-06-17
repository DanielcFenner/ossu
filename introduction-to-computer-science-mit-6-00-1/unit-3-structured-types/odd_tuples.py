def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTuple = ()
    for i in range(0, len(aTup), 2):
        newTuple += (aTup[i],)
    return newTuple