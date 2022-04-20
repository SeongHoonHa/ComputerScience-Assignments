import math
import itertools

##########################################################################
#PROBLEM 1
##########################################################################
#
#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    """ 
    Determine the number of n in log base 2
    Problem a5_1.1
    
    Args:
        positive number n

    Returns:
        number of n in log base 2
    """
    return math.log(n,2)            #converting the number in log base 2

#INPUT list of immutable objects
#RETURN probability distribution
def makeProbability(xlst):
    """ 
    Calculate the probability following the formula
    Problem a5_1.2
    
    Args:
        list of immutable numbers (not necessarily integers)

    Returns:
        list of probabilities for objects' counts
    """
    d = {}
    new_list = []
    
    for j in range(len(xlst)):          #counting the numbers in for loop
        if xlst[j] in d:
            d[xlst[j]] += 1
        else:
            d[xlst[j]] = 1
        
    for key in d:                       # putting the number in the dictionary
        new_list.append(d[key]/sum(d.values()))
    return new_list

#INPUT probability distribution
#RETURN non-negative number entropy
def entropy(xlst):
    """ 
    Getting the entropy following the formula
    Problem a5_1.3
    
    Args:
        list of probabilities for objects' counts

    Returns:
        entropy
    """
    p = 0
    for i in range(len(xlst)):          #calculating the entropy in for loop
        p += (xlst[i]*log_2(xlst[i]))   #adding up the calculations
    return -p                           #retrun -1 * the calculation following the formula



##########################################################################
#PROBLEM 2
##########################################################################
#INPUT positive integer
#RETURN positive integer
def magick(x):
    """ 
    Determine if the given number comes back after the calculation
    Problem a5_2
    
    Args:
        positive integer

    Returns:
        same positive integer after the calculation
    """
    y = 0
    y = ((x+15)*3-9)/3          #calculation following the steps of adding, multiplication, subtraction, and division
    return y - 12               #return y - 12 for the last step

##########################################################################
#PROBLEM 3
##########################################################################
#INPUT a list of lists of three positive integers [[a,b,c],[d,e,f],[g,h,i]]
#RETURN True if the input is a magic square
#You can create other functions to help you--they will 
#not be unit tested

def is_magic_square(s3):
    """ 
    Determine if the number list is vaild for magic square
    Problem a5_3.1
    
    Args:
        a list of lists of three positive integers

    Returns:
        validity of the list for magic square
    """
    if s3[0][0]+s3[0][1]+s3[0][2] != 15:            #determination of the exception for the magic square
        return False
    elif s3[1][0]+s3[1][1]+s3[1][2] != 15:
        return False
    elif s3[2][0]+s3[2][1]+s3[2][2] != 15:
        return False
    elif s3[0][0]+s3[1][0]+s3[2][0] != 15:
        return False
    elif s3[0][1]+s3[1][1]+s3[2][1] != 15:
        return False
    elif s3[0][2]+s3[1][2]+s3[2][2] != 15:
        return False
    elif s3[0][0]+s3[1][1]+s3[2][2] != 15:
        return False
    elif s3[0][2]+s3[1][1]+s3[2][0] != 15:
        return False
    else:
        return True

#INPUT nothing
#RETURN list of solutions to magic square size 3
def generate_3_square():
    """ 
    Generate the valid magic square number lists
    Problem a5_3.2
    
    Args:
        

    Returns:
        The lists of valid magic square number lists in range of 1 to 9
    """
    new_list = []
    p = itertools.permutations([1,2,3,4,5,6,7,8,9])                     #using intertools.permutations function to generate all the possible combinations in range of 1 to 9
    for i in p:
        square = [list(i[0:3]), list(i[3:6]), list(i[6:9])]             #dividing the list by 3 numbers
        if is_magic_square(square):
            new_list.append(square)                                     #append the list if it is valid combination for the magic square
    return new_list
        

        



##########################################################################
# PROBLEM 4
##########################################################################

#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    """ 
    encrypt the letters into the secrete code
    Problem a5_4.1
    
    Args:
        a sentence and a number of shift

    Returns:
        encrypted and shifted letters
    """
    return chr(ord(letter) + n)                                 #encrypting the letters shifted as many as n

#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    """ 
    decrypt the letters into the decoded secrete message
    Problem a5_4.2
    
    Args:
        letters and a number of shift

    Returns:
        decrpyted and shifted letters
    """
    return chr(ord(letter) - n)                                 #decrypting the letters shifted as many as n
#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    """ 
    Getting encrypted letters following the number of shift
    Problem a5_4.3
    
    Args:
        a sentence including lowercase letters and space and the number of shift

    Returns:
        encrypted letters
    """
    new_sentence = sentence.replace(" ", "{")                   #replacing space and {
    encrypted_string = ""
    for i in range(len(new_sentence)):
        encrypted_string += encrypt(new_sentence[i], shift)     #adding the strings
    return encrypted_string

#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    """ 
    Getting the decrypted sentence following the number of shift
    Problem a5_4.4
    
    Args:
        encrypted secret letters and the number of shift

    Returns:
        decrypted and shifted letters which shows the hidden message
    """
    decrypted_string = ""
    for i in range(len(sentence)):
        decrypted_string += decrypt(sentence[i], shift)         #adding the strings
    new_sentence = decrypted_string.replace("{", " ")
    return new_sentence

##########################################################################
# PROBLEM 5
##########################################################################

#INPUT non-negative integer and non-negative integer > 1
#RETURN Wild Number [string, base]
#string is encoding of number in base, base is integer
def make_number(decimal, base):
    """ 
    Getting the converted number following the base
    Problem a5_5.1
    
    Args:
        positive integer > 1

    Returns:
        a list of converted number and base
    """
    cnt = ""
    while True:
        cnt += str(decimal % 2)                 #adding string "1" in order
        decimal = decimal // 2                  #dividing decimal numbers by 2 in while loop
        if decimal == 0:                        #break condition
            break
    if base == 10:
        cnt = decimal
    return [cnt[::-1], base]                    #making it reverse so it can be shown as binary number
#INPUT Wild number 
#RETURN new wild number in new base
def convert(number, base):
    """ 
    converting number into the decimal system
    Problem a5_5.2
    
    Args:
        a number in binary notation

    Returns:
        a list of a decimal number and base
    """
    x = int(number[0],2)                        #using int(x,b) for converting binary number into decimal number
    x = str(x)
    return [x,base]
        


#INPUT two wild numbers
#RETURN product as a (possibly new) base
def mul_(number1, number2, base):
    """ 
    Multiply the numbers and show the result as follow the base
    Problem a5_5.3
    
    Args:
        two binary numbers and base

    Returns:
        a list of a multiplyed number and base
    """
    number1 = convert(number1, base)[0]         #converting binary number into decimal number
    number2 = convert(number2, base)[0]         #                   "
    multiply = int(number1)*int(number2)        #multiplying converted decimal numbers
    return [make_number(multiply,base)[0],base] #re-converting the multiplied decimal number into the binary notation

#INPUT two wild numbers
#RETURN sum as a (possibly new) base
def add_(number1, number2, base):
    """ 
    add the numbers and show the result as follow the base
    Problem a5_5.4
    
    Args:
        two numbers and base

    Returns:
        a list of the added number following the base and the base
    """
    list = []
    number1 = convert(number1, base)[0]         #converting binary number into decimal number
    number2 = convert(number2, base)[0]         #                    "
    add = int(number1)+int(number2)             #multiplying converted decimal numbers
    if base == 10:                              #if the base is already decimal, we don't have to convert the number
        list = [str(add),base]
    elif base == 2:                             #if the base is binary, we have to convert it as the binary number
        list = make_number(add, base)
    return list

# Problem 6

#INPUT path to amino acid file
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(file_path):
    """ 
    make a dictionary following the protein's name
    Problem a5_6.1
    
    Args:
        File path to "amino_acids.txt"

    Returns:
        protein dictionary
    """
    dictionary = {}
    with open(file_path, 'r') as someFile:
        content = someFile.readlines()
        for i in content:
            content = content.split(sep=',')
            if i[0].isupper == True and i[1].islower == True:
                amino_acid = i
            else:
                codon = tuple(i)
            dictionary[codon] = amino_acid
    return dictionary



    



#INPUT path to DNA file
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
def get_DNA(file_path):
    """ 
    getting a list of header and DNA
    Problem a5_6.2
    
    Args:
        File path to "DNA.txt"

    Returns:
        a list of header and DNA
    """
    list = []
    with open(file_path, 'r') as someFile:
        content = someFile.readlines()
        for i in content:
            if i[0:4] == ">HSG":
                header = i
            else:
                DNA = i
            list = list.append(header)
            list = list.append(DNA)
    return list

#INPUT FAST file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    """ 
    getting the simplified name of the protein
    Problem a5_6.3
    
    Args:
        file path to FAST file

    Returns:
        simplified name of the protein in string
    """
    pass

#Do not modify these statements

aa_d = {}   #the dictionary for the transation
DNA_d = []  #the FASTA file
protein = ''

def init_data(amino_acids_file, dna_file):
    global aa_d
    global DNA_d
    global protein
    aa_d = get_amino_acids(amino_acids_file)
    DNA_d = get_DNA(dna_file)
    protein = translate(DNA_d)


##########################################################################
if __name__ == "__main__":
    print("For your use...")
    actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"
    init_data("amino_acids.txt","DNA.txt")
    print("Please comment the code you want to run. Make sure it is inside of this if statement")
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")
    
    # print("*"*10 + "Problem 1"+"*"*10 +  "\n")
    # s0 = ["a", "b", "a", "c", "c", "a"]
    # s1 = ['a','b','a','b','a','b','b','b']
    # s2 = [(1),(2),(3),(4)]
    # s3 = [1]
    # s4 = [1,2,1,2]

    # xlst = [s0, s1,s2,s3,s4]

    # for i in xlst:
    #     p = makeProbability(i) 
    #     e = entropy(p)
    #     print(f"{p} has entropy {e}")

    # print("*"*10 + "Problem 2"+"*"*10 +  "\n")
    # s1 = [[2,7,6],[9,5,1],[4,3,8]] #True
    # s2 = [[8,1,6],[3,5,7],[4,9,2]] #True
    # s3 = [[8,6,1],[3,6,7],[4,9,2]] #False
    # s4 = [[1,1,1],[1,1,1],[1,1,1]] #False
    # s = [s1,s2,s3,s4]
    # for i in s:
    #     print("{0} is ".format(i) + "not "*(not is_magic_square(i)) + "a magic square." )
    # print(generate_3_square())

    # print("*"*10 + "Problem 4"+"*"*10 +  "\n")
    # sentence = "this is a secret message about the class"
    # shift = 5
    # secret = encrypt_sentence(sentence, shift)
    # decode_secret = decrypt_sentence(secret, shift)
    
    # print(f"original: {sentence}")
    # print(f"encrypted: {secret}")
    # print(f"decrypted: {decode_secret}")

    # print("*"*10 + "Problem 5"+"*"*10 +  "\n")    
    # n1,n2 = 5,4
    # base2, base10 = 2,10

    # x1, y1 = make_number(n1,base2), make_number(n2,base2)
    # print(x1,y1)
    # print(convert(x1,base10))
    # print(add_(x1,y1,base10))
    # print(add_(x1,y1,base2))
    # print(convert(add_(x1,y1,base2), base10))
    # print(mul_(x1,y1,base2))
    # print(convert(mul_(x1,y1,base2),base10))

    # print("*"*10 + "Problem 6"+"*"*10 +  "\n") 

    # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # should returns "D-"
    # print(translate(["nothing", "GACTAA"]))