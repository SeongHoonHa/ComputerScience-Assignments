
###############
# PROBLEM ONE
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


def get_data(path,name):
    """ 
    getting data from pop.txt
    Args:
    path (string)
    name (string)

    Returns:
    tmp (list)
    """
    tmp = []                            #making empty list to add
    pn = os.path.join(path, name)       #preparing to access file
    file = open(pn, "r")                #reading file
    for d in file:                      
        x,y = d.split(",")              #spliting values by comma
        tmp += [[int(x), int(y)]]       #making the values as integer and append them as list
    return tmp                          #returning completed data


def pop(year):
    """ 
    Calculating exponential function
    Args:
    selected year (integer)

    Returns:
    calculation result (float)
        
    """
    return 1436.53*((1.01395)**year)    #calculating following the formula

def error(data):
    """ 
    Calculating percentage of the average relative error
    Args:
    Data of years and population (list)

    Returns:
    Result of the calculation (float)
        
    """
    sum = 0                                     #making value to sum up
    for [year , pops] in data:                  #accessing elements in list in for loop
        sum += abs(pops-pop(year))/pops         #summation of the calculation in absolute value
    return (100/len(data))*sum                  #returning result that is the average of the summation in percentage



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    # data = get_data(".", "pop.txt")
    # total_error = round(error(data),4)

    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #     ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Growth. Total ave error = %{0}".format(total_error))
    # ax.grid()
    # plt.show()

###############
# PROBLEM TWO
###############
import csv

def my_int(xstr):
    """ 
    adjusting values if it is empty string
    Args:
    xstr (string)

    Returns:
    returning values (int)
        
    """
    if xstr == "":                      #if it is empty string
        return 0                        #converting as 0
    else:
        return int(xstr)                #otherwise, making string to integer
        
#INPUT state and state dictionary of data
#RETURN give the total confirmed deaths for 
# entire state
def scd(state,dic):
    """ 
    Accessing total number for confirmed death of the state
    Args:
    state (string)
    dic (dictionary)

    Returns:
    total number of confirmed death (integer)
        
    """
    sum = 0                         #setting up a default value for summation
    for (s,c) in dic:               #accessing tuple element in dictionary in for loop
        if s == state:              #finding input state in dictionary as a key
            sum += dic[(s,c)][1]    #summing the confirmed death caes for the state
    return sum                      #returning the result

#INPUT dictionary data and interval (a,b)
#RETURN all confirmed county cases greater than or equal to a
#and strictly less than b
def ccc(dic,interval):
    """ 
    making a dictionary of state-county mapped to confirmed cases
    Args:
    dic (dictionary)
    interval (tuple)

    Returns:
    dictionary of state-county mapped to confirmed cases (dictionary)
        
    """
    empty_dic = {}                                                              #setting up an empty dictionary to fill in
    for (s,c) in dic:                                                           #accessing tuple keys in dictionary in for loop
        if dic[(s,c)][0] >= interval[0] and dic[(s,c)][0] < interval[1]:        #making a condition following the interval
            empty_dic[(s,c)] = dic[(s,c)][0]                                    #filling in new dictionary keys and values in the interval
    empty_dic[(interval[0],interval[1])] = len(empty_dic)                       #adding the result of the number of conditionally satisfied states with interval at the end of the dictionary
    return empty_dic                                                            #returning complete dictionary

#INPUT state, data dictionary, state population
#RETURN state death density: confirmed deaths / population of state
#as a percentage to 3 places use round(x*100,3)
def sdd(state, dic,state_pop):
    """ 
    getting a percentage of death density
    Args:
    state (string)
    dic (dictionary)
    state_pop (dictionary)

    Returns:
    percentage of the death density (float)
        
    """
    confrimed_death = scd(state,dic)        #getting the number of confirmed death by using scd function
    s_pop = state_pop[state]                #accessing the number of the state population in dictionary
    density = confrimed_death/s_pop         #getting the density following (confirmed death cases) / (state population)
    return round(density*100,3)             #retunring the result by making it percentage and rounding it in thousandth decimal point

#INPUT data dictionary and state population 
#RETURN return the entire US death density
def usdd(dic,state_pop):
    """ 
    making a dictionary of entire death density in the US
    Args:
    dic (dictionary)
    state_pop (dictionary)

    Returns:
    dictionary that includes death densities of states in the US (dictionary)
        
    """
    empty_dic = {}                                      #setting up an empty dictionary to fill in
    for state in state_pop:                             #accessing state in state population dictionary in for loop
        empty_dic[state] = sdd(state,dic,state_pop)     #filling in the empty dictionary with death densities of each states
    return empty_dic                                    #returning completed dictionary
def get_dic(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a tuple
    The value for each key (also described in the document): a list of size 2 (both need to be integers)

    To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
    If you want to do it another way, please ask before attempting to use a method not talked about in class.

    HINT: You will need to skip the first row. 
            If you use a CSV reader, you can skip a row by doing `next(reader, None)`
    """
    """ 
    making a dictionary by accessing us-countries.csv file 
    Args:
    file path to access us-counties.csv file (string)

    Returns:
    completed dictionary that includes the information of county, state, confirmed case, and confirmed death (dictionary)
        
    """
    dic = {}                                                        #making an empty dictionary to fill in
    file = open(file_path,"r")                                      #opening file
    next(file)                                                      #ignoring first line of us-counties.csv file
    for d in file:                                                  #accessing neccessary keys and values in the file by using for loop
        _,county,state,_,_,_,c_case,c_death,_,_ = d.split(",")      #stating the keys and their values while spliting the values
        if c_case == "":                                            #making empty value as 0 if there is nothing between commas
            c_case = 0
        if c_death == "":                                           #making empty value as 0 if there is nothing between commas
            c_death = 0
        dic[(state,county)]=[int(c_case),int(c_death)]              #filling in the empty dictionary
    return dic                                                      #returning completed dictionary


def get_state_pop(file_path):
    """
    Reading from the file passed in, 
    extract the following information into a dictionary and RETURN a dictionary. 

    The key for the dictionary (also described in the document): a string
    The value for each key (also described in the document): an integer

    To read the file, you can do it the way we have seen before or using csv.reader. https://docs.python.org/3/library/csv.html#csv.reader 
    If you want to do it another way, please ask before attempting to use a method not talked about in class.
    """
    """ 
    making a dictionary that contains the most recent population for each state
    Args:
    file path to access sp.csv file (string)

    Returns:
    completed dictionary that contains the population of each states (dictionary)
        
    """
    dic = {}                                    #making an empty dictionary to fill in
    file = open(file_path,"r")                  #opening file
    for d in file:                              #accessing the values in the file by using for loop
        pop_list = d.split(",")                 #spliting the values in the file
        if len(pop_list) <= 1:                  #making an exception for the empty line in the file
            break
        dic[pop_list[0]] = int(pop_list[-1])    #filling in the dictionary with the states as keys and the recent populations as values
    return dic                                  #returning completed dictionary



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    # """

    #Our solutions used these two dictionaries 
    # has state, county, confirmed case, comfirmed deaths 
    # has state *most* current population 
    # dic = get_dic("us-counties.csv")
    # state_pop = get_state_pop("sp.csv")

    #county confirmed cases
    # intervals = [(0,1),(1,2),(0,2)]
    # c0 = ccc(dic,intervals[0])
    # c1 = ccc(dic,intervals[1])
    # c2 = ccc(dic,intervals[2])
    # if c0:
    #     print(f"Number of state-counties {intervals[0]} is {c0[intervals[0]]}")
    # if c1:
    #     print(f"Number of state-counties {intervals[1]} is {c1[intervals[1]]}")
    # if c2:
    #     print(f"Number of state-counties {intervals[2]} is {c2[intervals[2]]}")
    # max = float('inf')
    # cm = ccc(dic,(266380,max))
    # print(">= 266380 confirmed cases")
    # print(cm)

    # #state confirmed deaths
    # print(f"Alabama: {scd('Alabama', dic)}")
    # if state_pop:
    #     print(f"Alabama state pop: {state_pop['Alabama']}")
    # print(f"Alabama death density: {sdd('Alabama', dic, state_pop)}%")
    # print(f"{round((8166 / 4903185)*100, 3)}%")

    # #entire country death density percentage
    # x = usdd(dic,state_pop)
    # if x:
    #     print(f"Alabama: {x['Alabama']}%")
    #     print(x["Texas"])

###############
# PROBLEM THREE
###############
import math 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
simpson takes a function,beginning and ending points a and b, and the number of intervals
 over which to estimate the integration

 for example, we might define a function

 def some_function(x): 
     return 3*x*x + 1

 and estimate the integral from 0 to 6 with 100 steps

 simpson(some_function,0,6,100)
 """

def simpson(fn,a,b,n):
    """ 
    calculation result following Simpson's Rule formula
    Args:
    fn (funtion)
    a (integer)
    b (integer)
    n (integer)

    Returns:
    calculation result (float)
        
    """
    delta_x = (b-a)/n               #defining delta x
    sum = 0                         #setting up the default value to sum up
    for i in range(0,n+1):          #setting up for loop following the interval
        x_i = a + i*delta_x         #defining xi calculation
        if i == 0 or i == n:        #making a condition for the first and last calculation of the integral
            sum += fn(x_i)
        elif i % 2 != 0:            #making a condition for the coefficient of odd order of the integral
            sum += 4*fn(x_i)
        else:
            sum += 2*fn(x_i)        #making a condition for the coefficient of even order of the integral
    return ((b-a)/(3*n))*sum        #returning the calculation result following the formula
        
            

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print statements. 
    """

    # data = [[lambda x:3*(x**2)+1, 0,6,2],
    #         [lambda x:x**2,0,5,6],
    #         [lambda x:math.sin(x), 0,math.pi, 4],
    #         [lambda x:1/x, 1, 11, 6]]


    # for d in data:
    #     f,a,b,n = d
    #     print(simpson(f,a,b,n))

    # t = np.arange(0.0, 10.0,.1)
    # fig,ax = plt.subplots()
    # s = np.arange(0,6.1,.1)
    # ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    # plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    # ax.grid()
    # ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    # title = r"Area under the curve $\int_0^6\,f(x)$")

    # plt.show()