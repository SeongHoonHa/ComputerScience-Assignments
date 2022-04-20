import random as rn
import math

#############################################
# Problem 1
#############################################
def lr(xlst):
    """
    Args:
    xlst(list)

    Returns:
    max (int)
    
    Implement function described in the homework PDF
    """
    count = 1                           #defining current count
    max = 0                             #defining maximum count
    for i in range(len(xlst)-1):        #making for loop to check consecutive 1s
            if xlst[i] == 1:            
                if xlst[i] == xlst[i+1]:#comparing with next number in list
                    count += 1          #if it is consecutive, adding 1
                elif xlst[i] != xlst[i+1]:#if it is not consecutive, making it as default
                    count = 1
                if max < count:           #updating maximum count
                    max = count
    return max                              #returning the number of maximum count

#############################################
# Problem 2
#############################################
def nn(x,y,z):
    """
    Args:
    x (list)
    y (int)
    z (int)

    Returns:
    close_list (list)
    
    Implement function described in the homework PDF
    """    
    close_list = []                             #making an empty list to append
    
    for _ in range(z):                          #looping as many as z
        abs_list = []                           #defining an empty list to append the calculation in absolute value
        for i in range(len(x)):
            abs_value = abs(x[i]-y)             #defining the calculation
            abs_list.append(abs_value)          #making the list of the result
        for j in range(len(abs_list)):          #looping in newly created list to find the closest number
            closest_value = min(abs_list)       #defining the closest value
            if abs_list[j] == closest_value:    #finding the index
                close_list.append(x[j])         #appending the number in the close_list
                x.remove(x[j])                  #removing the number to make exception
                break                           #once it found, break
    return close_list                           #returning the result

#############################################
# Problem 3
#############################################
#Assume this is in 2D dimension
def distance(p1,p2):
    """
    Args:
    p1 (tuple)
    p2 (tuple)

    Returns:
    float
    Given two points, find the distance between the points.
    The points are given as a tuple with 2 values
    """
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5       #returning the calculation following the formula



def brute(xlst):
    """
    Args:
    xlst (list)

    Returns:
    list

    Given a list of points, where each points is represented 
    by a tuple of 2 values. 
    """
    tuple_1 = xlst[0]                           #defining the element for the first tuple
    tuple_2 = xlst[1]                           #defining the element for the second tuple
    min_diff = distance(xlst[0],xlst[1])        #defnining min_diff value
    for i in range(len(xlst)):                  #making a for loop to find minimum value
        for j in range(i+1,len(xlst)):          #making a for loop that making it efficient by excepting unneccessary calculation
            diff = distance(xlst[i],xlst[j])    #defining the calculation
            if diff < min_diff:                 #updating min_diff
                min_diff = diff
                tuple_1 = xlst[i]               #defining the first tuple that makes the minimum value
                tuple_2 = xlst[j]               #defining the second tuple that makes the minimum value
    return [tuple_1, tuple_2, min_diff]         #returning result as a list

#############################################
# Problem 4
#############################################
class Vector2D:
    def __init__(self, *x):
        if x:
            self.tuple_value = x
        else:
            self.tuple_value = (0,0)

    def get_tuple(self):
        return self.tuple_value

    def __mul__(self, other):
        """
        Args:
        self (instance of class)
        other (instance of class)

        Returns:
        result (integer)
        Implement function described in the homework PDF
        """
        x = self.get_tuple()            #accessing self instance
        y = other.get_tuple()           #accessing other instance
        result = x[0]*y[0]+x[1]*y[1]    #defining the calculation
        return result                   #returning the calculation result

    def __add__(self, other):
        """
        Args:
        self (instance of class)
        other (instance of class)

        Returns:
        instance of class 
        Implement function described in the homework PDF
        """
        x = self.get_tuple()                    #accessing self instance
        y = other.get_tuple()                   #accessing other instance
        return Vector2D(x[0]+y[0],x[1]+y[1])    #returning the calculation result

    def __sub__(self, other):
        """
        Args:
        self (instance of class)
        other (instance of class)

        Returns:
        instance of class
        Implement function described in the homework PDF
        """
        x = self.get_tuple()                    #accessing self instance
        y = other.get_tuple()                   #accessing other instance
        return Vector2D(x[0]-y[0],x[1]-y[1])    #returning the calculation result

    def __abs__(self):
        """
        Args:
        self (instance of class)

        Returns:
        float
        Implement function described in the homework PDF
        """
        x = self.get_tuple()                    #accessing self instance
        result = math.sqrt(x[0]**2 + x[1]**2)   #defining the calculation following the formula
        return result                           #returning the calculation result
    def scalar_mul(self, x):
        """
        Args:
        self (instance of class)
        x (int)

        Implement function described in the homework PDF
        """
        self.tuple_value = (self.tuple_value[0]*x,self.tuple_value[1]*x)    #defining the calculation of scalar multiplication
        
    def __neg__(self):
        """
        Args:
        self (instance of class)

        Implement function described in the homework PDF
        """
        self.tuple_value = (self.tuple_value[0]*-1,self.tuple_value[1]*-1)      #defining the calculation of negation


    def __eq__(self, other):
        """
        Args:
        self (instance of class)
        other (instance of class)

        Returns:
        Boolean
        Implement function described in the homework PDF
        """
        x = self.get_tuple()                    #accessing self instance
        y = other.get_tuple()                   #accessing other instance

        return x[0] == y[0] and x[1] == y[1]    #returning boolean: if the comparison is shown as the same, return True
                                                #if the comparison is not shown as the same, return False

    def __str__(self):
        return "{0}".format(self.get_tuple())


#############################################
# Main
#############################################
if __name__ == "__main__": 
    """

    """
    # Problem 1
    print()
    print("*"*30)
    print("* Problem 1")
    print("*"*30)
    x = [0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0]
    print(lr(x))



    # Problem 2
    print()
    print("*"*30)
    print("* Problem 2")
    print("*"*30)
    x = [1,2,3,4,5,6,7,8,9,10]
    y = 5
    z = 3

    print(x,y,z)
    print(nn(x,y,z))

    # Problem 3
    print()
    print("*"*30)
    print("* Problem 3")
    print("*"*30)


    x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    print("x", x)
    print("Distance between x[0] and x[1]: ", distance(x[0], x[1]))
    print("Brute:", brute(x))

    # Problem 4 
    print()
    print("*"*30)
    print("* Problem 4")
    print("*"*30)
    x = Vector2D(1,2)
    y = Vector2D(4,-1)
    w = Vector2D(1,2)
    print("Addition: ", x + y)
    print("Multiplication: ", x * y)
    print("Subtraction: ", x - y)
    print("Absolute value: ", abs(x))
    x.scalar_mul(5)
    print("Scalar Multiplication: ", x)
    -x
    print("Negative (1st): ", x)
    -x
    print("Negative (2nd): ", x)
    print("Equivalence: ", x == w)


