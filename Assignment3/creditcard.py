"""
    C200 Assignment 3: Credit Cards

    Author: Seong Hoon Ha

    Date:   Sep 21th, 2021

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

from random import randint
from creditcard_part1 import last_digit, decimal_right_shift


def verify(number13):                           
    n_list = list(map(int, str(number13)))        # spliting numbers in the list

    for i in range(len(n_list)):                  # finding numbers to be doubled in order
        if i % 2 == 1:
            n_list[i] = n_list[i]*2 
    
        
    n_sum = 0
    for i in range(len(n_list)):                  # adding 10 digit number with 1 digit number
        if n_list[i] // 10 >= 1:
            n_sum += decimal_right_shift(n_list[i]) + last_digit(n_list[i])
        else:
            n_sum += n_list[i]

        
    if n_sum % 10 == 0:                           # Checking if the 13 numbers are valid
        return True
    else:
        return False



    

    
    
    




def generate(number6):
    if not number6.isdigit():                     # Checking if the input number is digits
        return number6 + " is not all digits"


    if int(number6) > 999999 or int(number6) < 100000:        # checking if the input numbers are 6 numbers
        return number6 + " is not six digits"
    
    result = []                                    # checking if the combination of input numbers and random numbers are vaild in verify function
    while len(result) < 3:                         # making stop while loop until it finds 3 vaild combinations of numbers
        x = randint(1000000, 9999999)
        y = int(str(number6)+str(x))
        if verify(y) == True:
            result.append(y)

        


    return "Three valid numbers:\t" + str(result[0]) + "\t" + str(result[1]) + "\t" + str(result[2])    
        





# Possible return values
#
# "<num> is not all digits"
#
# "<num> is not six digits"
#
# "Three valid numbers:"
# "\t<num1>"
# "\t<num2>"
# "\t<num3>"
def main():
    base = input("Enter a 6 digit number:\n")
    print(generate(base))                              # I added print in order to check if my code works fine
    return generate(base)
    


if __name__ == "__main__":
    main()
