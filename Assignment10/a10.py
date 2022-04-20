import random as rn
import math

#############################################
# Problem 1
#############################################
def sel_sqrt(a,b):
    """ 
    Args:
    a (intger)
    b (intger)

    Returns:
    list of floats
    """
    return [i ** 0.5 if i % 2 != 0 else i *2 for i in range (a,b+1)]    #calculation following the conditions with inclusive interval of a and b in for loop

def inchtomtuple_lc(hlist_in):
    """ 
    Args:
    hlist_in (list)

    Returns:
    list of tuples
    """
    return [(i,round(i*0.0254,4)) for i in hlist_in]        #making list of tuples with calculation by using for loop

def intomtuple_map(hlist_in):
    """ 
    Args:
    hlist_in (list)

    Returns:
    list of tuples
    """
    return list(map(lambda x: (x,round(x*0.0254,4)),hlist_in))      #making list of tuples with calculation by using map and lambda

#############################################
# Problem 2
#############################################
def bmi_calc(weight, height):
    """ 
    Args:
    weight (integer)
    height (integer)

    Returns:
    float
    """
    return round(703*(weight/(height**2)),2)        #folloinwg the calculation and rounding
    
def bmi_lc(blist):
    """ 
    Args:
    blist (list)

    Returns:
    list of floats
    """
    return [round(bmi_calc(w,h),2) for (w,h) in blist]      #making list of the results with list comprehension

def bmi_map(blist):
    """ 
    Args:
    blist (list)

    Returns:
    list of floats
    """
    return list(map(lambda t: round(bmi_calc(t[0],t[1]),2),blist))      #making list of the results with map function and lambda function
                                                                        #since lambda takes tuple, I put t[0] and t[1] in bmi_calc function

def bmi_cat(bmilist):
    """ 
    Args:
    bmilist (list)

    Returns:
    list of floats
    """
    return [(bmi,"Underweight") if bmi < 18.5 else (bmi,"Normal Weight") if 18.5 <= bmi < 25 else (bmi,"Overweight") if 25 <= bmi < 30 else (bmi,"Obese") for bmi in bmilist]   #making list of results by using list comprehension with if/else conditions

#############################################
# Problem 3
#############################################
def bubble_sort(a):
    """ 
    Args:
    a (list)

    Returns:
    list of sorted integers array
    """
    for i in range(len(a)):                 #making for loop in range of the list
        for j in range(len(a)-1):           #making another for loop to sort
            if a[j] > a[j+1]:               #comparing integers if it is bigger than the next integer
                a[j], a[j+1] = a[j+1],a[j]  #sorting

    return a

def wbubble_sort(a):
    """ 
    Args:
    a (list)
    Returns:
    list of sorted integers array
    """
    i = 0                                       #setting up i value for while loop
    while i < len(a):                           #setting up while loop range
        j = 0                                   #setting up j value for another while loop
        while j < len(a)-1:                     #setting up another while loop for comparison in sorting process
            if a[j] > a[j+1]:                   #comparing integers if it is bigger than the next integer
                a[j], a[j+1] = a[j+1], a[j]     #sorting
            j += 1                              #looping
        i += 1                                  #looping
    return a
#############################################
# Problem 4
#############################################
def rsel_sort(xlst):
    """ 
    Args:
    xlst (list)
    Returns:
    list of sorted integers array
    """
    def recursive_sort(original,sorted):
        """ 
        Args:
        original (list)
        sorted (list)
        Returns:
        list of sorted integers array
        """
        if original == []:                              #making turning point for recursive loop
            return sorted                               #return empty list as a turning point
        else:
            sorted.append(min(original))                #appending minimum element of the original list
            original.remove(min(original))              #removing appended element from the original list
            return recursive_sort(original,sorted)      #looping as a recursive
    return recursive_sort(xlst,[])                      #returning list of sorted integers array

#############################################
# Main
#############################################
if __name__ == "__main__": 
    # Problem 1a
    print("sel_sqrt")
    print(sel_sqrt(0,10))
    print(sel_sqrt(10,15))
    print(sel_sqrt(15,20),"\n")

    # Problem 1
    print("Heights")
    heights = []

    for i in range(10):
        heights.append(rn.randint(48,90))
    print(heights)

    print(inchtomtuple_lc(heights))
    print(intomtuple_map(heights),"\n")

    # Problem 2
    print("BMI")
    wh = []
    for i in range(10):
        wh.append((rn.randint(100, 300), heights[i]))
    print(wh)

    print("bmi LC: ", bmi_lc(wh))
    print("bmi Map: ", bmi_map(wh))
    print("bmi Cat: ", bmi_cat(bmi_map(wh)))

    # Problem 3 
    print("Bubble Sort") 
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print(test)

    print(bubble_sort(test))
    print(wbubble_sort(test),"\n")

    # Problem 4
    print("Selection Sort")
    test = []

    for i in range(10):
        test.append(rn.randint(0,100))
    print(test)
    print(rsel_sort(test))

