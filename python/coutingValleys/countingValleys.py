#unsolved
from operator import eq 

steps = 8
path = 'DDUUUUDD'

#each step up or down represents 1 unit change in altitude / 
#stepUp = step+1 stepDown = step-1

#mountain is a sequence of consecutive steps above sea level starting 
#with a step up form sea level and ending with a step down to sea level
#if step>0: mountain

#valley is a sequence of consecutive steps below sea level, starting 
#with a step down from sea level and ending with a step up to sea level
#if step<0: valey

#given a sequence up and down steps during a hike, find and print the
# number of valleys walked through.

def countingValleys(steps, path):
    
    seaLevel = valley = 0

    for i in range(0, steps):
        if eq(path[i], "D"):
            seaLevel = seaLevel - 1
        else:
            seaLevel = seaLevel + 1

        if eq(path[i], "D") and seaLevel==0:
            valley+=1
        
    return valley     
