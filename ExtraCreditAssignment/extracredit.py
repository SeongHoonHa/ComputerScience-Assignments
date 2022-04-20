import math


###########################################################################
# Functions for Problem 1
###########################################################################

# This function will return a tuple of 2 values
# The "plus" value must be first in the tuple
# The "minus" value must be second in the tuple 
# The unit test expects ((v+u),(v-u)) **not** ((v-u),(v+u))
def q(a,b,c):
    """
    getting two (+,-) solutions for quadratic equation
    Args:
    a : integer
    b : integer
    c : integer


    Returns:
    final_function_first : float
    final_function_second : float

    """

    discriminant = b**2-4*a*c                       #discriminant value in the root
    root_value = math.sqrt(abs(discriminant))       #defining the root value in the formula (making discriminant value as an absolute value in case of it is negative)
    if discriminant < 0:                            #if discriminant value is negative
        root_value *= 1j                            #multiply 1j (i)
        
    first_value = -1*b + root_value                 #numerator when it is +
    second_value = -1*b - root_value                #numerator when it is -
    final_function_first = first_value / (2*a)      #completed calculation of the first solution
    final_function_second = second_value / (2*a)    #completed calculation of the second solution

    return (final_function_first, final_function_second)    #returning both solutions in tuple



###########################################################################
# Functions for Problem 2
###########################################################################
def checkout(xlst):
    """
    calculating total amount of the price
    Args:
    xlst : list


    Returns:
    amt : float

    """
    amt = 0                                 #making default value for summation
    for [amount,price,tax] in xlst:         #accessing list elements in xlst
        if tax == 1:                        #if tax should be calculated
            amt += amount*price*(1.07)      #multiply 1.07 for each element
        else:
            amt += amount*price             #otherwise, just multiply amount and price
    return amt                              #return total amount


###########################################################################
# Functions for Problem 3
###########################################################################
def open_seat_count(xlst):
    """
    checking opened and closed seat
    Args:
    xlst : list


    Returns:
    cnt : integer

    """
    cnt = 0                                 #making default value for summation
    for long_seat in xlst:                  #in range of lists in a big list
        for individual_seat in long_seat:   #in small lists
            if individual_seat == 0:        #if the seat is opened
                cnt += 1                    # +1 count
    return cnt                              #return total number of open seats
###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    """
    calculating arithmetic mean of numbers
    Args:
    nlst : list


    Returns:
    arithmetic mean : float

    """
    sum = 0                             #making default value for summation
    for number in nlst:                 
        sum += number                   #adding all the numbers
    return round(sum / len(nlst) , 2)   #dividing my the length of nlst and round in hundredth decimal point

def geo_mean(nlst):
    """
    calculating geometric mean of numbers
    Args:
    nlst : list


    Returns:
    geometric mean : float

    """
    a = math.e                          #defining exponential value
    sum = 0                             #making default value for summation
    for number in nlst:                 
        sum += math.log(number,a)       #adding numbers following log base and value
    mean = a**(sum/len(nlst))           #calculating the mean following the formula
    return round(mean,2)                #returning the mean by rounding up in hundredth decimal point

def har_mean(nlst):
    """
    calculating harmonic mean of numbers
    Args:
    nlst : list

    Returns:
    harmonic mean : float

    """
    sum = 0                         #making default value for summation
    for number in nlst:
        sum += 1/number             #getting sum following the formula
    return round(len(nlst)/sum,2)   #returning the mean following the formula and rounding up in hundredth decimal point
def RMS_mean(nlst):
    """
    calculating RMS mean of numbers
    Args:
    nlst : list


    Returns:
    RMS mean : float

    """
    sum = 0                                     #making default value for summation
    for number in nlst:
        sum += number**2                        #adding squared numbers following the formula
    return round(math.sqrt(sum/len(nlst)),2)    #returning the mean following the formula and rounding up in hundredth decimal point


###########################################################################
# Functions for Problem 5
###########################################################################

#INPUT ISBN string, assume "D-DDD-DDDDD-D" 
# D is digit
#RETURN Boolean if valid ISBN
def valid_ISBN(ISBN_str):
    """
    checking if the ISBN number is valid number
    Args:
    ISBN_str : string


    Returns:
    return value : boolean

    """
    pure_digit = ISBN_str.replace("-","")       #replacing "," so that I can get pure digits
    cnt = 0                                     #making default value for summation
    for i in range(len(pure_digit)):            #for loop in range of the digits
        cnt += int(pure_digit[i])*(i+1)         #adding values following the formula
    if cnt % 11 != 0:                           #if the summation result is not multiple of 11, it is not valid ISBN number. 
        return False                            #Therefore, return False.
    else:                                       #if the summation result is multiple of 11, it is valid ISBN number.
        return True                             #Therefore, return True.



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.
    You **do not** have to put anything here
    """
    print(q(1,-2,-4))
    print(checkout([[1, 1.45, 1],[3, 4.24, 1], [2, 14.00, 0], [4, 1.25, 1]]))
    print(open_seat_count([[1,0,0],[1,1,1],[1,1,0]]))
    print(geo_mean([2,4,8]))
    print(har_mean([1,2,3]))
    print(RMS_mean([1,3,4,5,7]))
    print(valid_ISBN("0-691-11321-1"))