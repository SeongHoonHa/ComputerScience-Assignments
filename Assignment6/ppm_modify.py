"""
    C200 Homework Assignment 6 : ppm modify

    Author: Seong Hoon Ha

    Date:   October, 15, 2021

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt

def color_translate(line):
    # TODO:
    #  write the complete docstring of this function.
    # For part 1
    # Inputs a single line (string) stripped and translates
    # the values as defined in the handout. 
    # returns a string
    """ 
    Translate the number into RGB value
    Problem a6_1
    
    Args:
        a line of numbers (string)

    Returns:
        a translated line of numbers in string (string)
    """
    empty_string = ""               #make empty string to add translated numbers
    line_split = line.split()       #separate the numbers to tranlsate
    for l in line_split:
        if int(l) % 3 == 0:
            empty_string += "0 "
        elif int(l) % 3 == 1:
            empty_string += "153 "
        elif int(l) % 3 == 2:
            empty_string += "255 "
    return empty_string.strip()         #earasing space at the end

def process_ppm(in_filename, out_filename, filter):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement the process function as specified in the handout
    """ 
    translate the file in RGB value and creat the updated file
    Problem a6_2
    preparing to re-create the lines of numbers in RGB values
    Args:
        ppm file of numbers including headers before translation (input file name, out file name, filter function)

    Returns:
        translated and re-written file of translated numbers in RGB value (new file)
    """
    filtered_content = []                   #making an empty list to add the numbers
    with open(in_filename, 'r') as rgb:     #reading the file
        header1 = rgb.readline()            # separating headers in order to maintain its value
        header2 = rgb.readline()            #               "
        header3 = rgb.readline()            #               "
        content = rgb.readlines()
        for i in content:
            filtered_content.append(filter(i))      #appending the translated values before re-creating the file
    with open(out_filename, "w") as filtered:       #opening the file before re-writing
        filtered.write(header1)
        filtered.write(header2)
        filtered.write(header3)
        for j in filtered_content:
            filtered.write(j+"\n")                  #re-writing the translated values in a new file
        




def main_part1():
    # TODO: call the <decode> function you developed to decode
    #  the image <files/part1.ppm>
    """ 
    operating the translation code
    Problem a6_3    
    Args:
        input file

    Returns:
        translated file as an output
    """
    process_ppm("files/part1.ppm", "files/part1_output.ppm", color_translate)       #applying the translation function

def grey_scale(line):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement the grey_scale function as specified in the handout
    """ 
    translate the values in grey scale following the formula
    Problem a6_4
    
    Args:
        a line of number in string (string)

    Returns:
        translated values in grey scale (string)
    """
    empty_string = ""                               #creating empty string to add the translated values
    line_split = line.split()                       #spliting the numbers before translation
    for i in range(0, len(line_split), 3):          #distinguishing values to translate in its own formula
        r = int(line_split[i])
        g = int(line_split[i+1])
        b = int(line_split[i+2])
        grey = int(sqrt(r**2+g**2+b**2))            #putting in the translation formula
        if grey > 255:                              #making an execution for the abnormal value over 255
            grey = 255
        grey_str = str(grey) + " "                  #defining how to put the translated values
        empty_string += grey_str*3                  #adding up the translated values in the empty string
    



    return empty_string.strip()
def main():
    # TODO: implement the following required items:
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. Perform grey_scale conversion on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    4. WRite the complete docstring
    """
    """ 
    introduction for the grey scale translation (including input file name and output file name)
    Problem a6_5
    
    Args:
        ppm file path to translate in grey scale

    Returns:
        new created ppm file translated in grey scale
    """
    in_file_name = input("input file name:")            #inputting the file path with message
    out_file_name = input("output file name:")          #naming the output file's name
    process_ppm(in_file_name, out_file_name, grey_scale)#applying the translation function


if __name__ == '__main__':
    #main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1

