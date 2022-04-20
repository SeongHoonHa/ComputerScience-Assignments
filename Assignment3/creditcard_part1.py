"""
    C200 Assignments 3: Credit Cards, Part 1

    Name: YOUR-NAME-HERE
   
    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

def last_digit(num):
    """Computes the last digit of the num

    Args:
        num (int): A positive integer

    Returns:
        (int) : The last digit of num (123 -> 3)
    """
    
    num = num % 10                                         # I got the remain to extract first digit number
    return num

# Right shifts num by one digit
#  123 -> 12
def decimal_right_shift(num):
    num = num // 10
    return num


# Sum digits of the input -- assume there
# are exactly three digits
def sum_digits(num):
    num = num[0]+num[1]+num[2]                              # I splited numbers and added them
    return num

    

# Ask the user for input and print a message
# Three possible messages:
#    "Number must be all digits"
#    "Number must be three digits"
#    "The sum of the digits of <num> is <result>"
def main():
    num = input("Please enter a 3-digit positive number:\n\t")
    if int(num) <= 99 or int(num) >= 1000:                 # Checking if the input number is 3 digit number
        print("Number must be three digits")
    elif int(num) >= 100 or int(num) <= 999:               
        num = int(num)
        print("The sum of the digits of " + str(num) +" is "+str((num // 100 + (num // 10 % 10) + num % 10)))
    else:
        print("Number must be all digits")
    

if __name__ == "__main__":
    main()
