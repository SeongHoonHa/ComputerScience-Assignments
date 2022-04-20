#############################################
# Problem 1
#############################################
def F(n,m,p):
    """
    making recursive loop for the formula
    Args: 
    n : integer
    m : integer
    p : integer


    Returns:
    calculation result : integer

    """
    if p == 0:                          #turning back point
        return 100+n-m                  #return value of the point
    else:
        return n*m-p+F(n-3,m-2,p-1)     #calculation for recursive loop

def Ft(n,m,p,v = 100):
    """
    making tail recursive loop for the formula
    Args:
    n : integer
    m : integer
    p : integer


    Returns:
    calculation result : integer

    """
    if p == 0:                          #turning back point
        return n-m+v                    #return value of the point
    else:
        return Ft(n-3,m-2,p-1, v+n*m-p) #calculation for tailed recursive loop and saving summation in "v" parameter

def B(n):
    """
    making recursive loop for the formula
    Args:
    n : integer

    Returns:
    calculation result : integer

    """
    if n == 0:                          #turning back point
        return 5                        #return value of the point
    elif n == 1:                        #second turning back point (because we also have to consider when n is 1)
        return 10                       #return value of the point
    else:
        return 5*n+B(n-1)               #calculation for recursive loop

def Bt(n,v=0):
    """
    making tail recursive loop for the formula
    Args:
    n : integer


    Returns:
    calculation result : integerw

    """
    if n == 0:                          #turning back point
        return v + 5                    #return value of the point
    elif n == 1:                        #second turning back point
        return v + 10                   #return value of the point
    else:
        return Bt(n-1,v+5*n)            #calculation for tailed recursive loop and saving summation in "v" parameter


def x(n):
    """
    making recursive loop for the formula
    Args:
    n : integer

    Returns:
    calculation result : integer
    """
    if n == 0:                      #turning back point
        return 3                    #return value of the point
    elif n % 2 == 0:                #condition when n value is an even number
        return 2*n+1+x(n-1)         #calculation
    elif n % 2 != 0:                #condition when n value is an odd number
        return 2*n+x(n-1)           #calculation

def xt(n,v=3):
    """
    making tail recursive loop for the formula
    Args:
    n : integer

    Returns:
    calculation result : integer
    """
    if n == 0:                      #turning back point
        return v                    #return value of the point
    elif n % 2 == 0:                #condition when n value is an even number
        return xt(n-1,v+2*n+1)      #calculation
    elif n % 2 != 0:                #condition when n value is an odd number
        return xt(n-1,v+2*n)        #calculation

#############################################
# Problem 2
#############################################
d,c = "d","c"
def balance(xbook):
    """
    Comparing credit balance and debit balance
    Args:
    xbook : list

    Returns:
    result if credit balance is equal to debit balance : boolean
    """
    debit_sum = 0                       #making default debit balance sum value to add
    credit_sum = 0                      #making default credit balance sum value to add
    for [type,amt] in xbook:            #accessing list elements in xbook list
        if type == "d":                 #if the type is debit
            debit_sum += amt            #separately add debit values
        elif type == "c":               #if the type is credit
            credit_sum += amt           #separately add credit values
    return credit_sum == debit_sum      #if the comparison result is same, return True. If not, return False

def balance_rec(xbook):
    """
    Comparing credit balance and debit balance by using recursive loop
    Args:
    xbook : list

    Returns:
    result if credit balance is equal to debit balance : boolean
    """
    def bh(blst):
        if not blst:                                #turning back point
            return 0                                #return value of the point
        else:
            if blst[0][0] == "d":                   #limiting condition when it is debit balance
                return bh(blst[1:]) + blst[0][1]    #adding debit balances only
            elif blst[0][0] == "c":                 #limiting condition when it is credit balance
                return bh(blst[1:]) - blst[0][1]    #subtracting credit balances only

    return not bh(xbook)                            #if the result is 0 it means debit balance - credit balance is 0, which means both values are same. Therefore, it results True ("not" works as the correction for the boolean). Else, it results False.



#############################################
# Problem 3
#############################################
def gsf_close(a,r,n):
    """
    calculating values following the formula
    Args:
    a : numeric value
    r : numeric value
    n : integer

    Returns:
    result of the calculation : numeric value

    """
    return a*((1-r**n)/(1-r))               #returning result following the formula

def gsf(a,r,n):
    """
    calculating values following the formula with for loop
    Args:
    a : numeric value
    r : numeric value
    n : integer

    Returns:
    result of the calculation (sum) : numeric value
    """
    sum = 0                                 #making default value for the summation
    for i in range(n):                      #setting up for loop as many as n value
        sum += a*(r**i)                     #adding all values starting from n=0
    return sum                              #returning the sum

def g(a,r,n):
    """
    calculating values following the formula with recursive loop
    Args:
    a : numeric value
    r : numeric value
    n : intger


    Returns:
    result of the calculation : numeric value

    """
    def gh(k):
        """

        Args:
        k : integer

        Returns:
        result of the calculation : numeric value
        
        """
        if k == 0:                          #turning back point
            return a                        #returning value of the point
        else:
            return a*(r**k)+gh(k-1)         #calculation for the recursive loop

    return gh(n-1)                          #returning the calculation result

#############################################
# Problem 4
#############################################
def occurs(x,xlst):
    """Problem 4.  For loop implementation of occurs

    Args:
        x (number): value
        xlst (list): list of values

    Returns:
        found: boolean (True or False)
    """
    found = False
    for i in xlst:
        if x == i:
            found = True
            break
    return found

def occurs_w(x,xlst):
    """
    checking if x value is in xlst with while loop
    
    Args:
    x : value
    xlst : list

    Returns:
    found : boolean
    """
    i = 0                       #making default i value for while loop
    found = False               #making default condition for boolean
    while i < len(xlst):        #setting up i range in while loop
        if xlst[i] == x:        #if the loop finds x value in xlst
            found = True        #making found as True
            break               #stop while loop
        i += 1                  #looping to the next value in xlst
    return found                #returning the result as boolean
        

def occurs_r(x,xlst):
    """
    checking if x value is in xlst with recursive loop

    Args:
    x : value
    xlst : list

    Returns:
    boolean (If x is found, result is Ture. If not, result is False)

    """ 
    if xlst:                                            #making if condition in xlst
        return x == xlst[0] or occurs_r(x,xlst[1:])     #checking if x value exists in xlst[0]. If not, move on to the next position of xlst
    
    else:
        return False                                    #if x does not exist in xlst, return False

#############################################
# Problem 5
#############################################
def gcd(x,y):
    """
    finding the greatest common divisor of x and y
    Args:
    x : integer
    y : integer

    Returns:
    the greatest common divisor : integer

    """
    if y > x:                       #changing x and y position if y value is greater than x value
        a = x
        b = y
        x = b
        y = a
    elif y == 0:                    #turning back point
        return x                    #returning value of the point
    else:
        return gcd(y, x%y)          #getting the greatest common divisor by using recursive loop
if __name__ == "__main__": 
    # Problem 1
    print("The next 3 lines are calls for F and Ft")
    print(F(5,5,5),Ft(5,5,5))
    print(F(1,2,3),Ft(1,2,3))
    print(F(5,4,2),Ft(5,4,2))
    
    print("The next 5 lines are calls for B and Bt")
    for i in range(5):
       print(B(i), Bt(i))
       
    print("The next 5 lines are calls for x and xt")
    for i in range(5):
           print(x(i),xt(i))

    # Problem 2  
    d,c = "d","c"
    xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
    xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
    print(balance_rec(xbook1),balance(xbook1))
    print(balance_rec(xbook2), balance(xbook2))

    # Problem 3
    print(gsf(2,3,5))
    print(g(2,3,5))
    print(gsf_close(2,3,5))

    #Problem 4
    print(occurs(1,[2,3,4]),occurs_w(1,[2,3,4]),occurs_r(1,[2,3,4]))
    print(occurs([1],[1,3,4]),occurs_w([1],[1,3,4]),occurs_r([1],[1,3,4]))
    print(occurs([1],[1,[1],2]),occurs_w([1],[1,[1],2]),occurs_r([1],[1,[1],2]))

    # Problem 5
    print(gcd(10,6))
    print(gcd(12,9))
    print(gcd(55,40))

