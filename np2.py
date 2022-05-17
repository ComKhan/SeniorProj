def np2 (value):
    
    var = value
    count = 0
    i = 0
    nextpow2 = 0
    while i == 0:
        var = var >> 1
        count = count + 1
        if var == 0:
            i = 1
            
    nextpow2 = pow(2,count+1)        
    return nextpow2