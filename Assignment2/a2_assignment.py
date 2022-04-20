import math

def s(speed_limit):
    """ Compute the modified speed limit as an integer
    Problem a2_1

    Args:
        speed_limit (int) : speed in mile/hour 
    
    Returns:
        int : modified speed limit
    """
    
    if  speed_limit >= 55:
        return speed_limit + 5
    elif speed_limit >= 45:
        return speed_limit + 3
    elif speed_limit >= 30:
        return speed_limit + 1
    else:
        return speed_limit

def E(m):
    """
    Compute the energy for a mass given Einstein's equation E = MC^2
    Problem a2_2

    Args:
        m (float) : mass in kilograms
    
    Returns:
        float : energy
    """
    c = 3e8 #uses scientific notation
    return m*((3*(10**8))**2)

def f(fuel_price, money, gas_mileage, distance):
    """ 
    Determine if we have enough money for the trip
    Problem a2_3
    
    Args:
        fuel_price (float): Price of fuel (dollars/gallon)
        money (float): Available money (dollars)
        gas_mileage (float): Fuel economy (miles/gallon)
        distance (float): distance to travel (miles)

    Returns:
        bool : Returns True if the available money is sufficient
    """
    if (gas_mileage*(money/fuel_price) - distance) >= 0:
        return True
    else:
        return False


    

#PROBLEM 4 a2_4
#INPUT angle (degrees), length, length
#RETURN length of opposite side
def law_cosines(angle, len_1, len_2):
    # Add Proper Comments (see examples above)
    return ((len_1)**2+(len_2)**2-2*(len_1)*(len_2)*math.cos((angle*math.pi)/180))**0.5

#PROBLEM 5 a2_5a
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
#INPUT two numbers
#RETURN maximum of the two
def max(x,y):
    # Add Proper Comments
    if x > y:
        return x
    else:
        return y

#PROBLEM 5 a2_5b
#You must use your max function
#INPUT non-empty list of numbers
#RETURN maximum number in list
def max_3(x,y,z):
    # Add Proper Comments
    if y > z:
        return max(x,y)
    elif z > y:
        return max(x,z)
    elif x > y:
        return max(z,x)
    elif y > x:
        return max(z,y)
    elif x > z:
        return max(y,x)
    elif z > x:
        return max(y,z) 
    

#PROBLEM 5 a2_5c
#You can *only* use if, elif, and else (or some combination)
#INPUT 3 numbers
#RETURN maximum number in list
def max_3h(x,y,z):
    # Add Proper Comments
    if x > (y and z):
        return x
    elif y > (x and z):
        return y
    elif z > (x and y):
        return z

#PROBLEM 6 a2_6
#INPUT pair of strings for colors:
# "yellow", "blue", "red", "green", "purple", and so on
#RETURN either a color when c1, c2 are the same
#or the 2ndary color given primary colors
#or "unknown" otherwise
def color_wheel(c1,c2):
    # Add Proper Comments
    if c1 == c2:
        return c1
    elif c1 == "blue" and c2 == "yellow":
        return "green"
    elif c1 == "yellow" and c2 == "blue":
        return "green"
    elif c1 == "blue" and c2 == "red":
        return "purple"
    elif c1 == "red" and c2 == "blue":
        return "purple"
    elif c1 == "red" and c2 == "yellow":
        return "orange"
    elif c1 == "yellow" and c2 == "red":
        return "orange"
    else:
        return "unknown"
     

#PROBLEM 7 a2_7a
#INPUT radius of circle in inches
#RETURN area of circle
def pizza_area(radius):
    # Add Proper Comments
    return (radius**2)*(math.pi)

#PROBLEM 7 a2_7b
#INPUT r1, c1 (radius and cost of pizza 1)
#      r2, c2 (radius and cost of pizza 2)
#RETURN the radius of the pizza that's cheaper
#You must use the pizza_area function 
def cost_per_inch(r1,c1,r2,c2):
    # Add Proper Comments
    pizza_1 = pizza_area(r1)
    pizza_2 = pizza_area(r2)
    if (pizza_1/c1) > (pizza_2/c2):
        return r1
    else:
        return r2



def pretty(asn):
    """ Print header for output of each problem

    Args:
        asn (anythong): the problem number
    """
    print(10*"~" + "problem " + str(asn) + 10*"~")

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    pretty(1)
    print(s(60),s(50),s(40),(20))

    pretty(2)
    print("{:.0e}".format(E(.1)))
    
    pretty(3)
    print(f(1, 7.50, 10, 200))
    print(f(1, 20.00, 10, 200))
    print(f(3, 20.00, 10, 200))
    print(f(3, 20.00, 35, 200))

    pretty(4)
    print(law_cosines(50,3,4))
    print(law_cosines(47,9,10))
    print(law_cosines(90,5,5))

    pretty(5)
    print(max_3(1,2,3))
    print(max_3(3,2,1))
    print(max_3(1,3,2))
    print(max_3h(1,2,3))
    print(max_3h(3,2,1))
    print(max_3h(1,3,2))

    pretty(6)
    print(color_wheel("yellow", "blue"))
    print(color_wheel("blue", "yello"))
    print(color_wheel("yellow", "yellow"))
    print(color_wheel("orange", "yellow"))

    pretty(7)
    print(cost_per_inch(18,10,12,7))
    print(cost_per_inch(18,10,12,5))
    print(cost_per_inch(18,10,12,4))