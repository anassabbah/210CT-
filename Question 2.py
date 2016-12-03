#Trailing 0s in a factorial number
def trailing(n):
    fivecount = 0 #increments fivecount
    for i in range (2, n+1): 
        while i > 0:  #whilst i is greater than 0
            if i % 5 == 0: #checks if i remainder 5 is the equivalent to 0
                fivecount += 1 #increment fivecount
                i = n	/5
            else:
                break
    return fivecount
