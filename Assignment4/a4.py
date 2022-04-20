"""
CS200 Assignment 4 
   Practice with iterables
"""

import math

if __name__ == "__main__":
    print()
    print("Currently running `a4.py`")
    print("The output presented here is just extra print information; the output you see in the terminal is for reference—not for final grading")
    print("To determine if functions work properly, refer to the testing file")

#####################################################################################################
#PROBLEM ONE
#####################################################################################################

#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is a block
# if n = 0, then return ""
def block(n):                                       
    x = n*(n*"*"+"\n")                              #adding stars with \n per number of n in order to make filled block
    if n == 0:
        x == ""
    return x


#INPUT non-negative integer n
#RETURN string of * that, when printed,
# is an outline 
# if n = 0, then return ""
def square(n):
    first_low = (n*"*"+"\n")                        #making first line of square
    middle_low = "*"+(n-2)*" "+"*"+"\n"             #making hollow space as many as "n"
    last_low = n*"*"                                #making last line of square
    hollow_square = first_low+(n-2)*middle_low+last_low
    if n == 1:                                      #making an exception
        hollow_square = "*"
    elif n == 0:                                    #making an exception
        hollow_square == ""

    return hollow_square


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 1")
    for i in range(5):
        print("Block of size {0}".format(i))
        print(block(i))
    

    for i in range(5):
        print("Square of size {0}".format(i))
        print(square(i))
   

#####################################################################################################
#PROBLEM 2
#####################################################################################################

#DATA
## DO NOT CHANGE THESE VARIABLES MANUALLY
act, Au,Ag,Pd,Pt ="act", "gold", "silver", "paladium", "platinum"
spot_price = {Au:1833.15, Ag:27.61, Pt:1275.20, Pd: 2426.60}
portfolio = {act: 10000}
portfolio["holdings"] = {Au:(0,0), Ag:(0,0), Pt:(0,0), Pd: (0,0)}

#INPUT portfolio, metal, and number of ounces of metal
#RETURN True or False
#True: transaction has been made
#False: transaction has not been made  
def purchase(portfolio, metal, amt):
    price = spot_price[metal]*amt               #defining price
    if portfolio[act] >= price:
        portfolio[act] -= price                 #updating account
        portfolio["holdings"][metal] = (amt+portfolio["holdings"][metal][0], spot_price[metal]*amt+portfolio["holdings"][metal][1])
        return True
    else:
        return False
           





#INPUT portfolio and metal
#RETURN non-negative integer of number of ounces
#that can be purchased
def how_much(porfolio, metal):
    return porfolio[act]// spot_price[metal]        # deciding if the remained account is enough to buy the metal

    

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 2")
    print(purchase(portfolio,Au, 1))
    print(portfolio)
    print(purchase(portfolio,Au, 1000))
    print(portfolio)

    purchase(portfolio,Au, 2)
    purchase(portfolio,Ag,3)
    purchase(portfolio,Pt,2)
    print(portfolio)
    print(how_much(portfolio, Pd))

#####################################################################################################
#PROBLEM 3
#####################################################################################################

#INPUT a possibly empty list of numbers
#RETURN the smallest number and the number of times
#it occurs in the list
def find_num_min(xlst):
    if len(xlst) == 0:                #making an exception
        return ()
    else:
        minimum = min(xlst)
        cnt = 0
        for i in xlst:
            if minimum == i:
                cnt = cnt + 1           #updating the number of the minimum number
        return (minimum,cnt)
 

    



if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 3")
    x1 = []
    x2 = [1,0,0,1]
    x3 = [1,2,3,4,0]
    x4 = [5]
    x5 = [-1,0,2,2,0,-1]

    x = [x1,x2,x3,x4,x5]
    for i in x:
        print(find_num_min(i))

#####################################################################################################
#PROBLEM 4
#####################################################################################################
#Solving cryptarithms

#INPUT None
#RETURN list of all possible solutions
def search_me_me_bee():
    for B in range(0,10):
        for E in range(0,10):
            for M in range(0,10):
                if 10*M + E + 10*M + E == 100*B + 10*E + E:
                    if not M in [B,E] and not E in [E,M] and not B in [E,M]:
                        return B,E,M

#INPUT None
#RETURN list of all possible solutions
def search_go_to_out():
    for T in range(0,10):
        for O in range (0,10):
            for G in range (0,10):
                for U in range (0,10):
                    if 10*T + O + 10*G + O == 100*O + 10*U + T:
                        if not T in [O,G,U] and not O in [T,G,U] and not G in [T,O,U] and not U in [T,O,G]:
                            return T,O,G,U


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 4")
    print(search_me_me_bee())
    print(search_go_to_out()) 

#####################################################################################################
#PROBLEM 5
#####################################################################################################

#INPUT a (possibly empty) list of integers
#RETURN the length of the longest monotonic sequence
def increase(xlst):
    max_cnt = 0                             
    cnt = 0
    for i in range(len(xlst)-1):
        if xlst[i] <= xlst[i+1]:
            cnt += 1                        #updating count
        else:
            cnt = 0                         #defaulting count
        if cnt > max_cnt:                   
            max_cnt = cnt               #completing the final number of max count
    return max_cnt
 


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 5")
    x1 = [0,1,2,2,3,1,2,3,1,1,0,1]
    x2 = [1,2,3,4,5,0,1,1,1,1,1,1,1,1]
    x3 = [1,2,3,4,5,1]
    x4 = [5,4,3,2,1]
    xlst = [x1,x2,x3,x4, []]
    for i in xlst:
        print("Longest monotonic sequence in {0}: \n{1}".format(i,increase(i)))

#####################################################################################################
#PROBLEM 6
#####################################################################################################

#INPUT string of containing only letters, spaces, comma, and period
#RETURN a dictionary that gives the count of each letter
def letter_count(text):
    text = text.lower()                 #making the letters in low case
    letter = {}                         #adding dictionary

    for i in text:                      
        if i in letter:                 #counting the numbers following dictionary
            letter[i] += 1
        else:
            letter[i] = 1               #if the number of letter is one
    return letter


    



if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 6")
    f ="Two roads diverged in a yellow wood,\
        And sorry I could not travel both\
        And be one traveler, long I stood\
        And looked down one as far as I could\
        To where it bent in the undergrowth"
    g = "the quick brown fox jumped over the lazy dog"
    print(letter_count(f))
    print(letter_count(g))

#####################################################################################################
#PROBLEM 7
#####################################################################################################

#INPUT two vectors of same length
#RETURN dot product
def dot_prod(x,y):

    return sum(x*y for x,y in zip(x,y))             #grouping x,y with zip and multiply each other, then adding all of them with sum()
    

#INPUT vector and scalar
#RETURN vector 
def scalar_vec(x,n):
    list = [i*n for i in x]                         
    return list

#INPUT vector
#RETURN non-negative scalar (float or real)
def euc_len(x):
    sum = 0
    for i in range(len(x)):                        #caculating all the numbers in the list
        sum += x[i]**2
    return sum**0.5

#INPUT two vectors
#RETURN the angle in DEGREES between 
def ang_vec(x,y):
    return (math.acos( (dot_prod(x,y)/(euc_len(x)*euc_len(y)))))*(180/math.pi)      #following the formula
        

#INPUT vector
#RETURN uni vector
def unit_vec(x):
    list = [i/euc_len(x) for i in x]                #folloing the formula with the numbers in the list
    return list

#INPUT two vectors and either "+" or "-"
#RETURN sum or difference of vectors
def vec_op(x,y,op):
    op_list = []
    if op == "+":
        op_list = [x+y for x,y in zip(x,y)]         #adding each other when op is +
    elif op == "-":
        op_list = [x-y for x,y in zip(x,y)]         #deducting each other when op is -
    return op_list

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 7")
    # Vectors
    x = [4,3]
    y = [3,5]

    print(vec_op(x,y,"+"))
    print(vec_op(x,y,"-"))
    print(dot_prod(x,y))
    print(scalar_vec(x,1/5))
    print(euc_len(x))
    print(euc_len(y))
    print(ang_vec(x,y))
    print(unit_vec(x))
    print(euc_len(unit_vec(x)))


#####################################################################################################
#PROBLEM 8
#####################################################################################################

# https://www.michigan.gov/documents/dnr/TreeAge_401065_7.pdf

def tree_age(circumferance, bark, growth_rate):
    radius = (circumferance[0]*12+circumferance[1])/math.pi*0.5-bark            #defining the length of radius following the formula
    return round(radius/growth_rate)


def noninvasive_tree_age(circumferance, tree):
    tree_rate = {"White Oak": 5.0, "Red Oak": 4.0, "Pin Oak": 3.0, "Linden": 3, "Basswood": 3.0}        #making a dictionary to use
    radius = ((circumferance[0]*12+circumferance[1])/math.pi*0.5)                                       #getting the age of specific tree following the formula
    return round(radius/(1/tree_rate[tree]))

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 8")
    print("\ttree_age")
    print(tree_age([12,10], .5, .2))
    print(tree_age([1,1],0,.3))
    print("\tnoninvasive_tree_age")
    print(noninvasive_tree_age([12,10], "White Oak"))
    print(noninvasive_tree_age([5, 5], "Red Oak"))


#####################################################################################################
#PROBLEM 9
#####################################################################################################

#INPUT list of int, str, set, tuple, lists...
#RETURN list of unique values in list
#REQUIREMENTS cannot use Python set or set functions
#Can use in predicate
def make_unique(xlst):
    list = []
    for i in xlst:
        if i not in list:           #removing already exist word or number
            list.append(i)          #adding in the empty list
    return list



#INPUT list and size
#RETURN returns a list of list of size
#if there is left over that's less than
#size, then make the a list
def partition(xlst, size):
    list = []
    sub_list = []
    if size == 0:           #making an exception
        return []
    for i in range(len(xlst)):
        sub_list.append(xlst[i])
        if len(sub_list) == size:       #spliting by the size
            list.append(sub_list)       #adding them in the empty list
            sub_list = []
    if len(sub_list) >= 1:              #adding the remain at the end of the list
        list.append(sub_list)
    return list




#INPUT list and object
#RETURN all the locations of object in the list
#REQUIREMENTS Cannot use any list functions
def occurs_at_index(xlst, item):
    list = []
    for i in range(len(xlst)):
        if xlst[i] == item:         #finding the position of the number "item"
            list.append(i)          #adding in the empty list
    return list



#INPUT two lists x,y
#RETURN list of *unique* objects that belong to both lists
#REQUIREMENTS cannot use Python set, set functions
def intersect(xlst, ylst):
    list = []
    for x in xlst:              
        for y in ylst:             
            if x == y and not x in list:        #making condition to find same number
                list.append(x)                  #adding in the empty list
    return list


#INPUT list of numbers and int 0,1
#RETURN if int is 0, then find minimum
#if int is 1, then find maximum
#REQUIREMENTS cannot use Python max, min
#ERROR if list is empty, return []
def optimum(xlst,s):
    if xlst == []:                  #making an exception
        return []
    if s == 0:                  #when it finds the minimum
        min_x = xlst[0]
        for x in xlst:
            if x < min_x:
                min_x = x       #updating the smaller number in for loop
        return min_x
    if s == 1:                  #when it finds the maximum
        max_x = xlst[0]
        for x in xlst:
            if x > max_x:
                max_x = x       #updating the bigger number in for loop
        return max_x

        
            
        


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 9")
    print("\tmake_unique")
    x1 = [1,0,1,0,"dog", "cat", "cat", (1,),(1,),(2,)]
    x2 = [[],[],"","",(),()]
    print(make_unique(x1))
    x3 = []
    print(make_unique(x2))
    print(make_unique(x3))
    print("\tpartition")
    print(partition([1,2,3,4],0))
    print(partition([1,2,3,4],2))
    print(partition([1,2,3,4],1))
    print(partition([1,2,3,4],3))
    print(partition([1,2,3,4],4))
    print(partition([1,2,3,4],5))
    print("\toccurs_at_index")
    print(occurs_at_index([0,1,0,1,1],1))
    print(occurs_at_index([0,1,0,1,1],2))
    print(occurs_at_index([0,1,0,1,1],0))
    print("\tintersect")
    print(intersect([],[1]))
    print(intersect([2],[]))
    print(intersect([1,1],[1,1,2]))
    print(intersect([2,1,2,3],[3,1,3]))
    print("\toptimum")
    print(optimum([],0))
    print(optimum([],1))
    print(optimum([1],0))
    print(optimum([1],1))
    print(optimum([1,1,-1,100,-100],0))
    print(optimum([1,1,-1,100,-100],1))


#####################################################################################################
#PROBLEM 10
#####################################################################################################

#INPUT list of numbers 
#RETURN sum
def sigma(xlst):
    x = 0
    if xlst == []:      #exception
        return []
    for i in range(len(xlst)):
        x += xlst[i]                #adding all of them
    return x


#INPUT list of numbers
#RETURN sum of the squares
def sigma_square(xlst):
    x = 0
    if xlst ==[]:
        return []
    for i in range(len(xlst)):
        x += xlst[i]**2             #adding all of the squared numbers
    return x


#INPUT list of pairs of numbers [[x0,y0],[x1,y1],...,[xn,yn]]
#RETURN sum of the products x0*y0+x1*y1+...+xn*yn
#If list is empty, return []
def sigma_product(xlst,ylst):
    if xlst == [] and ylst == []:
        return []
    a = sum(x*y for x,y in zip(xlst,ylst))          #grouping x and y and adding all of the x*y numbers
    return a

#INPUT takes a list of lists
#RETURN returns list of slices [0:1], [1:2], ...
#of each list
#The ORDER of the ouput is critical -- look at the
#unit test please
def separate(xlst):
    if xlst == []:
        return []
    list1 = []
    for i in range(0,len(xlst[0])):                 #range is in between the first sublist length
        list2 =[]  
        for j in range(0,len(xlst)):                #range is in the entire list length
            list2.append(xlst[j][i])
        list1.append(list2)                         #appending all othe them in the bigger list
    return list1

        
        

   
        
    




#INPUT coefficents and input value to linear function
#RETURN predicted value
def linear_model(a,b,x):
    return a*x + b

#INPUT list of pairs d = [[x0,y0], [x1,y1], ... ]
#RETURN coefficients a,b as a tuple to 
#linear function f(x) = ax + b
def make_linear(xlst):
    pass


if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 10")
    print("\tsigma")
    print(sigma([]))
    print(sigma([1,2,-3,3]))
    print(sigma([100,10,1]))
    print("\tsigma_square")
    print(sigma_square([]))
    print(sigma_square([-1,1,1]))
    print(sigma_square([10,2,3]))
    print("\tsigma_product")
    print(sigma_product([1,2,3],[1,10,100]))
    print(sigma_product([-1,-2,3],[9,0,3]))
    print(sigma_product([],[]))
    print("\tseparate")
    print(separate([]))
    print(separate([[1],[2],[3],[4],[5]]))
    print(separate([[1,10],[2,20]]))
    print(separate([[1,10,100],[2,20,200],[3,30,300]]))
    print(separate([[1,1],[2,3],[4,3],[3,2],[5,5]]))


    print("** To see plot uncomment the lines below **")

    # d1 = [[43,99],[21,65],[25,79],[42,75],[57,87],[59,81]]
    # d2 = [[1,1],[2,3],[4,3],[3,2],[5,5]]

    # x,y = separate(d1)
    # print(x)
    # print(y)
    # a,b = make_linear(d1)
    # print(a,b)
    # x,y = separate(d2)
    # print(x)
    # print(y)
    # a,b = make_linear(d2)
    # print(a,b)

    # #Code to visualize data
    # #BEGIN
    # import matplotlib.pyplot as plt

    # x,y = separate(d2)

    # #plot data and line
    # x1 = list(range(1,6))
    # y1 = []
    # for i in x1:
    #     y1 += [linear_model(a,b,i)]
    # plt.scatter(x,y,color="red")
    # plt.plot(x1,y1)

    # #plot predicted points
    # for i in x:
    #     plt.scatter(i,linear_model(a,b,i),color="green")

    # #plot residuals
    # for i,j in d2:
    #     plt.plot([i,i],[j,linear_model(a,b,i)], linestyle =(0, (1, 1)), color="black" )

    # #text on plot   
    # plt.text(3.2,2.27,r"residuals $|y - f(x)|$")
    # plt.ylabel(r"$f(x) = {0}x + {1}$".format(a,b))
    # plt.xlabel('x')
    # plt.title("Linear Model")

    # #render to display
    # plt.show()

    # #END

#####################################################################################################
#PROBLEM 11
#####################################################################################################

#INPUT either list, string, or tuple
#RETURN reverse list, string, or tuple
#REQUIREMENTS cannot use slicing 
#to reverse string
#if the iterable is a number DD0..0, then the
#return discards the leading zeros DD
def reverse(x):
    if type(x) == str or type(x) == list or type(x) == tuple:       #finding if they are str, list, or tuple
        x_list = []                 #making empty list to append
        for i in range(len(x)-1, -1, -1):       #going backward
            x_list.append(x[i])
        if type(x) == tuple:                #when it is tuple
            return tuple(x_list)
        elif type(x) == list:               #when it is list
            return x_list
        else:
            return "".join(x_list)
    if type(x) == int:                      #when it is integer
        y = 0
        while x > 0:
            y = y*10 + (x % 10)
            x = x // 10 
        return y

        


        
    


#INPUT take a string
#RETURN True if the string is palindrome, False otherwise
#REQUIREMENTS treat letters as all lower case
#remove space, comma, period, question mark, exclamation
#point
def palindrome(x):
    x = x.replace(" ","").replace(",","").replace(".","").replace("?","").replace("!","")   #removing everything except letters
    x = x.lower()           #making letters in lower case

    if reverse(x) == x:
        return True         #printing True if x is palindrome
    else:
        return False        #printing False if x is not palindrome

if __name__ == "__main__":
    print("\n")
    print("===========================================================================")
    print("Problem 11")
    print("\treverse")
    xtest = ["abc", 120, (1,2,3), [1,2,3]]

    for i in xtest:
        print(reverse(i))

    print("\tpalindrome")
    xlst = ["Step on no pets.", "Was it a cat I saw?", "A",\
            "Eva, can I see bees in a cave?", "Uhh...", "Oreos yum!"]

    for i in xlst:
        print(palindrome(i))
