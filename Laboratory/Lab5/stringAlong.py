def stringFormatDocumentation():
    """
    This function will involve reading documentation. 
    This function does not return anything, it is more of a place to combine 
    code and comment out the function call in `__main__`
    """
    string1 = "{}-{}" 
    string2 = "{:>10}" 
    string4 = "Does {} == {} ? -> {}" 
    string5 = "{:~^10}" 
# print("{} - {}".format(n1,n2))
    strings = [string1, string2, string4, string5]

    resultStrings = [
        ["10 - 11", "12 - 13", "1 - 1", "4 - 4", "5 - 5"], # Results for string1
        ["      Star", "      Trek", "       TNG", " Hello   !"], # Results for string2
        ["Does 1 == 2 ? -> False", "Does 2 == 2 ? -> True", "Does A == B ? -> yes"], # Results for string4
        ["~~~C200~~~", "~~~WOW~~~~", "~~~~Oh~~~~", "~~~wOw~~~~"] # Results for string5
    ]

    args = [
        [[10, 11], [12, 13], [1, 1], [4, 4], [5, 5]], # Arguments for string1
        [["Star"], ["Trek"], ["TNG"], ["Hello   !"]], # Arguments for string2
        [[1, 2, False], [2, 2, True], ["A", "B", "yes"]], # Arguments for string4
        [["C200"], ["WOW"], ["Oh"], ["wOw"]]# Arguments for string5
    ] 

    for i in range(len(args)):
        print()
        print("\tString {} Tests".format(i + 1))
        currentArgs = args[i]
        curString = strings[i]
        resultString = resultStrings[i]
        for j in range(len(currentArgs)):
            yourString = curString.format(*currentArgs[j]) # What is this line? 
            # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists 
            # We will learn more about this in the semester but just allows you to provide the arguments without 
            # the programmer doing it themselves
            corrString = resultString[j]
            print("\t\tYour String vs Correct String:\n\t\t'" + yourString + "' vs '" +  corrString + "'\t\tMatches : " + str(yourString == corrString))


#### Student End Of Lab Functions here
def cap_strings(str_list):
    '''
    Count the number of capitalized strings in the list str_list
    parameters: str_list -> list of strings
    returns: int of the number of strings in all caps
    '''
    count = 0

    for string in str_list:
        for letter in string:
            if letter.upper():
                count += 1
    
    return count



def validPassword(password):
    """
    Given a string, determine if it's a valid password.
    To be valid the password must:
    - be at least 10 characters long
    - contain 1 uppercase character
    - contain 1 lowercase character
    - contain 1 digit
    - contain one special character
        - We can assume special characters include !,@,#,$,%,^,&,*,(,)
    """
    if len(password) < 10:
        return False
    
    upper = False
    lower = False
    digit = False
    special = False
    special_characters = ["!","@","#","$","%","^","&","*","(",")"]

    for letter in password:
        if letter.upper():
            upper = True
        if letter.lower():
            lower = True
        if letter.isdigit():
            digit = True
        if letter in special_characters:
            special = True
    
    if upper and lower and digit and special:
        return True
    return False


def youCodedWhat(pathToPythonFile):
    """
    Given a python file (you can read a python file in python), determine the following:
    - number of functions in the code
    - number of lines that are comments (whole line is a comment)
    - number of for loops
    - number of while loops
    - times you used the digit 1 (ex. `x = 111` is 3 1s)
    - times you used the number 2 (not digit) (ex. x = 222 does not count)

    Return this information in a dictionary

    Hint: the beginning of the line often has the piece of information you need (without white space)
    """
    d = {
            "functions": 0,
            "comments": 0,
            "for": 0,
            "while": 0,
            "1": 0,
            "2":0
        }
    
    with open(pathToPythonFile) as myFile:
        contents = myFile.readlines()

    for line in contents:
        if "def" in line:
            d["functions"] += 1
        
        if "#" in line or "\"\"\"" in line:
            d["comments"] += 1
        if "for" in line:
            d["for"] += 1
        if "while" in line:
            d["while"] += 1
        if "1" in line:
            d["1"] += 1
        if "2" in line:
            d["2"] += 1
    return line

    return d


if __name__ == "__main__":
    
    stringFormatDocumentation()
    print()
    print("cap_strings", "\t", cap_strings(["C200", "is", "the", "BEST", "class", "EVER"])) # Expected 3
    print()
    print("Valid Passwords")
    # https://www.lifewire.com/strong-password-examples-2483118
    tests = ["1Ki77y", "D3ltagamm@", "SerlGmail2.15", "!Lov3MyPiano", "!LoveMyPiano"]
    expected = [False, True, False, True, False]
    for t, e in zip(tests, expected):
        print("Testing: {} \t Retrieved: {} \t Expected: {}".format(t, validPassword(t), e))
    print()
    print("Your Code:")
    #print(youCodedWhat("Assignment6/a6.py")) # These are dependent on your file
    print(youCodedWhat("Assignment5/a5.py")) # These are dependent on your file


