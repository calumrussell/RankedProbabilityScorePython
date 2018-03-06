def rps(parr, res):
    r = len(parr)
    
    inner = 0;
    cump = 0;
    for i, p in enumerate(parr):
        cump+=p
        if i>=res:
            inner+=pow(cump-1, 2)
        else:
            inner+=pow(cump-0, 2)
    return (1/(r-1)) * inner

"""
 rps([0.5,0.25,0.25], 0)

 first param is list of probabilities, 
 second param is the index of result i.e. 0 if 0.5 wins
"""
