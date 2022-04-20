"""
    C200 Homework Assignment 7 : PPM Processing

    Name: Seong Hoon Ha

    Date:   2021, October 28th

    The goal of this assignment is to give you practice working with nested lists
    by writing a program that manipulates the entire image with multiple lines.
"""


def process(lines, rows, cols):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """ 
    Converting lines to the nested list by rows and columns
    
    Args:
        lines = list
        rows = integer
        cols = intger

    Returns:
        big_list = list      #converted list by rows and columns
    """
    big_list = []                                   #creating empty list in order to append small lists
    for row in range(rows):                         #making for loop looping as many as rows
        line = lines[row].split()                   #spliting "lines" as many as row loop
        small_list = []                             #creating empty list in order to append column elements
        for col in range(cols*3):                   #making for loop looping as many as columns and multiplying 3 following RGB
            small_list.append(int(line[col]))       #appending column elements and making the elements as integer
        big_list.append(small_list)                 #appending column lists in big list
    return big_list
        
    


def read_ppm(filename):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """ 
    reding and converting file with process function
    
    Args:
        filename = file path

    Returns:
        two_dimension_content = list     #converted rgb values to nested list by rows and columns
    """
    with open(filename, 'r') as rgb:                            #reading file
        header1 = rgb.readline()                                #reading first header   
        header2 = rgb.readline()                                #reading second header
        special_header2 = header2.split()                       #modifying header 2 following rows and columns
        cols = int(special_header2[0])                          #identifying column value
        rows = int(special_header2[1])                          #identifying row value
        header3 = rgb.readline()                                #reading third header
        content = rgb.readlines()                               #reading all the RGB values
        two_dimension_content = process(content,rows,cols)      #converting RGB values with process function
        return two_dimension_content                            #returning converted values
        


def write_ppm(image, filename):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """ 
    Creating converted version of ppm file
    
    Args:
        image = list
        filename = file path

    Returns:
        nothing (but creates modified file)
    """
    with open(filename, "w") as output_file:                    #writing a new file
        output_file.write("P3\n")                               #since P3 is fixed value, write P3 for the first line
        rows = len(image)                                       #identifying row value
        cols = len(image[0])//3                                 #identifying column value
        output_file.write(f"{cols} {rows}\n")                   #write column and row value by using f string function
        output_file.write("255\n")                              #since 255 is fixed value, write 25 5 for the third line
        for row in range(rows):                                 #making for loop looping as many as row value
            for col in range(cols*3):                           #making for loop looping as many as column value and multiplying 3 following RGB
                output_file.write(f"{image[row][col]} ")        #writing converted values
            output_file.write("\n")                             #organizing with \n
    
    
         


def scale(image, row_scale, col_scale):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """ 
    filtering rgb values by row scale and column scale
    
    Args:
        image = list
        row_scale = integer
        col_scale = integer

    Returns:
        big_list = list
    """
    rows = len(image)                               #identifying row value
    cols = len(image[0])//3                         #identifying column value
    big_list = []                                   #creating empty list in order to append small lists
    for row in range(0,rows,row_scale):             #making a loop looping as many as row value and slicing following row scale value
        small_list = []                             #creating empty list to append column values
        for col in range(0,cols*3,col_scale*3):     #making a loop looping as many as column value and slicing following column scale value
            small_list.append(image[row][col])      #appending R value
            small_list.append(image[row][col+1])    #appending G value
            small_list.append(image[row][col+2])    #appending B value
        big_list.append(small_list)                 #appending column lists in the big list
    return big_list                                     


def main():
    # TODO:
    """
    1. Ask the user for an input file name.
    2. Ask the user for an output file name.
    3. Ask the user for a height scaling factor.
    4. Ask the user for a width scaling factor.
        (Note that you should enforce both scaling factors
        must be positive integers)
    5. The program will read from the input file and create a
    new file with the specified name that contains a copy of the
    input file scaled down by the specified factors.
    """
    in_file_name = input("input file name:")                    #asking input file path
    out_file_name = input("output file name:")                  #asking output file name and path
    while True:                                                 #enforcing positive integer input
        height = int(input("input height scaling factor: "))    
        if height > 0:
            break
        else:
            print("Please input positive integer")              #generating while loop if the input value is not a positive integer
    while True:                                                 #enforcing positive integer input
        width = int(input("input width scaling factor: "))      
        if width > 0:
            break
        else:
            print("Please input positive integer")              #generating while loop if the input value is not a positive integer
    image = read_ppm(in_file_name)                              #defining converted and read file
    scaled_image = scale(image, height, width)                  #defining scaled file following input height and width values
    write_ppm(scaled_image, out_file_name)                      #creating a modified file



if __name__ == '__main__':
    main()
