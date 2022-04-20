"""
One of the code implementations for the problems in Lab3.py

I may add some more interesting functions such as append_prime_number
"""

# List Operations

def manual_append(list_one, element):
    '''
    given a list and an element append the element to the list 
    note to do this operation you can't use the .append method for lists

    inputs:
    list_one - a list of values can be any type
    element - a value of any type

    output:
    one coherent list of all elements combined

    '''
    list_one.append(element)

    return list_one

def manual_remove(list_one, val):
    '''
    given a list and a specific value remove the item and report wether you were successful 
    by using a for loop to iterate over the list

    inputs:
    list_one - list of specific type(int or str) 
    val - the value that you want removed

    output:
    list - the list with the element removed if the element is not found return the list
    '''
   # newlist = []

   # for i in list_one: # i =some element in list_one
   #     if i != val:
   #         newlist = newlist + [i]
    
   # return newlist

    newlist = []
   
    for i in range(len(list_one)):
        if list_one[i] != val:
            newlist = newlist + [list_one[i]] #element at position i

    return newlist

# Doing things with list data structures

def compare_lists(list_one, list_two):
    '''
    given 2 lists compare and report which indexes are different in an output list

    your output should look something like this: [1, 3, 5]
    
    which means that index 1, 3, and 5 are different values these lists can compare any data type

    inputs:
    list_one - list of a specific type (int or str) of length n
    list_two - list of a specific type (int or str) of length n

    outputs:
    list of ints which correlate to indexes that are different in a list
    '''
    newlist = []
    for i in range(len(list_one)):
        if list_one[i] != list_two[i]:

            newlist = newlist + [i] #newlist += [i]
    return newlist

def factorial_for(n):
    '''
    given a number calculate the factorial value using a for loop

    input:
    n - integer value that will be factorial you want to calculate 

    output:
    the calculated factorial of the input value 
    '''
    product = 1
    for i in range(1, n+1): # i = 1,2,3,4,5 for n = 5
        product = product * i

    return product


if __name__ == '__main__':
    # TODO:
    # implement testing
    list1 = [1, 3, 6, "a", 5, "b"]
    ele1 = "c"
    print(manual_append(list1, ele1))
    
    list2 = [1, 2, 3, 4, 5]
    ele2 = 5
    print(manual_remove(list2, ele2))

    list3 = ["a", "b", "c", 1, 2]
    list4 = ["a", 3, "c", 6, 7]
    print(compare_lists(list3, list4))
    # [1, 3, 4] --> list of positions

    print(factorial_for(5))
    print(factorial_for(10))