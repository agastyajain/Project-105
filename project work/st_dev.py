import math

data=[60,61,65,63,98,99,90,95,91,96]
squared_list = []

def mean(): 
    total = 0
    for i in data:
        total += i 
    mean = total / len(data)
    return mean

def squares():
    dif = 0
    for i in data:
        dif = i - mean()
        sq = dif * dif
        squared_list.append(sq)

def sumSquares():
    squares()
    sum = 0
    for i in squared_list:
        sum += i 
    sumSquares = sum
    return sumSquares

def st_dev():
    sum = sumSquares()
    quotient = sum/len(data)
    deviation = math.sqrt(quotient)
    print("The Standard Deviation of the given data is " + str(deviation))

st_dev()
