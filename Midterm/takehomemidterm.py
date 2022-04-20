import random as rn
import numpy as np

"""
Problem 1
"""
def unique_words(xstring):
    """Problem 1.  Find the unique words in a string

    Args: a sentence in string

    Returns: a list of unique words

    """
    empty_list = []
    replaced_string = xstring.replace('.',"").replace(',',"").lower()   #erasing period and comma sign and changing the letters in lower case
    complete_stringlist = replaced_string.split()       #making the string as a list
    for i in complete_stringlist:
        if i not in empty_list:
            empty_list.append(i)        #appending words that are not repeated
    return empty_list

def find_index(word, words_list):
    """My own function to find the index in list

    Args: a specific word string and word list

    Returns: the poistion of the word in the list
    """
    for i in range(len(words_list)):
        if words_list[i] == word:
            return i

def get_transition_matrix(xtr):
    """Problem 1.  Generate the transition matrix

    Args: a sentence in string

    Returns: a list of lists showing the transition matrix
    """
    
    replaced_string = xtr.replace(',',"").lower()       #erasing comma and making letters in lower case

    sentences = replaced_string.split(".")              #spliting sentences

    unique_list = unique_words(xtr)                     #generating unique words
    
    zero_list = [[0] * len(unique_list) for i in range(len(unique_list))]   #making default matrix

    for sentence in sentences:
        word_list = sentence.split()                        #spliting sentences
        for i in range(len(word_list)-1):
            first_word = word_list[i]                       #making a connection between two consecutive words
            second_word = word_list[i+1]                    #                       "
            row = find_index(first_word,unique_list)             #finding index number in the matrix
            col = find_index(second_word,unique_list)            #finding index number in the matrix
            zero_list[row][col] += 1                        #adding 1 per instance
    return zero_list

"""
Problem 2
"""
def running_average(xlist,per):
    """Problem 2.  Compute thr running average

    Args: a list of integers, period in integer

    Returns: a list of averages following the period

    """
    empty_list = []
    for i in range(len(xlist)-(per-1)):                     #range is different by the period
        average = 0                                         
        for j in range(per):
            average += round(xlist[i+j]/per,2)                       #adding up the averages in for loop and rounding to the nearest hundreth 
        empty_list.append(average)                          #appending in the empty list
    return empty_list
        
               

##########################################################################
if __name__ == "__main__":
    # Fill in with code to test your functions for both problems
    # Note that the np.array() function converts the list that is returned to 
    # a numpy array. This is only done for display/print purposes, so be sure that
    # your function returns a list.

    xtr = "The cat is in the house. The dog is outside playing with the kids. Both the dog and the cat need a bath. The kids need to come in and eat dinner."
    uniwords = unique_words(xtr)
    print(uniwords)
    print("There are {0} unique words in the text.".format(len(uniwords)))
    print(np.array(get_transition_matrix(xtr)))

    data = [11, 82, 91, 55, 32, 91, 12, 5]
    print(data)

    period = 3 # time period for running avg (3 day average)
    run_avg = running_average(data,period)

    print("The {0}-day running average is: {1}".format(period,run_avg))
