import math

#INPUT two values A,B
#Return A + B
#REQUIREMENTS 
def myPlus(A,B):
#TO DO: Implement function
    x = A+B
    return x
print( myPlus(2,3))

#INPUT two values A,B
#Return A - B
#REQUIREMENTS 
def myMinus(A,B):
#TO DO: Implement function
    x = A - B
    return x
print( myMinus(2,3) )
    

#INPUT two values A,B
#Return A divided by B
#REQUIREMENTS 
def myDivide(A,B):
#TO DO: Implement function
    x = A/B
    return x
print( myDivide(2,3))
    

#INPUT two values A,B
#Return A x B
#REQUIREMENTS 
def myProduct(A,B):
#TO DO: Implement function
    x = A*B
    return x
print ( myProduct(2,3))

#INPUT two values A,B
#Return A raise to the power of B
#REQUIREMENTS 
def myExponent(A,B):
#TO DO: Implement function
    x = A**B
    return x
print ( myExponent(2,3))

#INPUT two values A,B
#B is not zero
#Return The Bth root of A
#REQUIREMENTS: Use myExponent function
def myRoot(A,B):
#TO DO: Implement function
    x = A**(1/B)
    return x
print (myRoot(2,3))

#INPUT one non-negative value A and base x
#Return log base x of A
#REQUIREMENTS use math module
def myLog(A,x):
#TO DO: Implement function
    y = math.log(A,(x))
    return y
print (myLog(10,3))
    

#INPUT one value A
#Return absolute value of A
#REQUIREMENTS 
def myAbs(A):
#TO DO: Implement function
    x = abs(A)
    return x
print (myAbs(-2))

#INPUT one value A
#Return e raised to A (Euler's constant)
#REQUIREMENTS use math module
def myExp(A):
#TO DO: Implement function
    x = math.exp(A)
    return x
print(myExp(2))

#INPUT one value A
#Return floor of A, greatest integer less than A
#REQUIREMENTS use math module
def myFloor(A):
#TO DO: Implement function
    x = math.floor(A)
    return x
print(myFloor(3.15))