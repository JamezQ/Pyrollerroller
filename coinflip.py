import random
def flip(flips):
    """Flips a number of coins randomly, returns result in
    number of heads or tails, heads first."""
    heads = 0
    tails = 0
    for f in range(flips):
        flip = random.randint(0,1)
        if flip is 0:
            heads += 1
        else:
            tails += 1
    result = [heads,tails]
    return result


fliparray = []
#Start flipping the coins range(x) amount of times at flip(x) amount of coins at
#a time.
for i in range(1000000):
    fliparray.append(flip(18))
    
flipresult = []

#Count the number of occurances of each flip of x, x being whatever was sent to
#the flip function, such as flip(4) being print the count the occurances that
#four flips resulted in [2,2] two heads two tails, or so on.
for i in fliparray:
    try:
        flipplace = flipresult.index(i)
        flipresult[flipplace+1] += 1
    except ValueError:
        flipresult.append(i)
        flipresult.append(1)

switch = True
resultarray = []
resultitem = []
#Split the arrays
for i in flipresult:
    if switch:
        resultitem.append(i)
        switch = False
        continue
    resultarray.append(i)
    switch = True

results = sum(resultarray)
#Sort the values
for j in range(len(resultarray)):
    key = resultarray[j]
    key2 = resultitem[j]
    i = j - 1
    while (i >=0) and (resultarray[i] > key):
        resultarray[i+1] = resultarray[i]
        resultitem[i+1] = resultitem[i]
        i = i - 1
    resultarray[i+1] = key
    resultitem[i+1] = key2
    
resultarray.reverse()
resultitem.reverse()

#Print out all the values
for i in range(len(resultarray)):
    resultpercent = '%.12f' % ((resultarray[i]+0.0)/(results+0.0))
    resultpercent = resultpercent.rstrip('0')
    resultpercent = resultpercent[2:]
    if len(resultpercent) is 1:
        resultpercent += '0'
    if len(resultpercent) is 2:
        resultpercent += '%'
    else:
        resultpercent = resultpercent[:2] + '.' + resultpercent[2:] + "%"
    print '{0:7} {1:5} {2} {3}'.format(resultitem[i],resultarray[i],"=",resultpercent)
