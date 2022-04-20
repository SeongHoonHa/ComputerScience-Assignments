### Problem 1

def check_number(i,msg,low,high):
    """
    Checks that integer i is in correct range  low..high (inclusive)
    i (int) the number
    msg (s) error message fragment (one of 'Month', 'Day', or 'Year')
    low (int) low end of range
    high (int) high end of range

    returns i or raises ValueError(...)
    """
    """ 
    Args:
    i : integer
    msg : string
    low : integer
    high : integer

    Returns:
    returns "i" if it is in the range (integer)
    OR returns error message if it is not in the range (string)
    """
    if i >= low and i <= high:                  #checking if i is in range bewteen low and high (inclusive)
        return i                                #returning i if it is in the range
    else:
        raise ValueError(f'Invalid {msg} {i}')  #rasing error message 


def parse_date(s):
    """
    Checks that s is a valid date mm/dd/yyyy or mm-dd-yyyy
    Raises SyntaxError if form is wrong or mm, dd,
    yyyy are not digit strings with correct number 
    of digits.  
    Raises ValueError if mm, dd, yyyy are not in legal ranges 
    (checked in order mm, dd, yyyy)

    Returns (int(mm),int(dd),int(yyyy))
    """
    """ 
    Args:
    s (string)

    Returns:
    returns a tuple of month, day, and year if it is valid (tuple)
    OR returns errors messages (string)
    """
    split_s_slash = s.split("/")        #splitting s by slash
    split_s_dash = s.split("-")         #splitting s by dash

    syntax_message = SyntaxError(f'Incorrect Date Syntax {s}')          #defining error message with f string

    if len(s) != 10:            #length of s should be 10. Therefore, checking if its length is 10
        raise syntax_message    #if it's not, rasie the error message
    if len(split_s_slash) == 3: #length of splitted s should be 3 by month, day, and year
        if len(split_s_slash[0]) != 2 and len(split_s_slash[1]) != 2 and len(split_s_slash[2]) != 4:    #checking the length of the month, day, and year
            raise syntax_message    #if it is not valid, raise the error message
        try:                                #trying the splitted elements in the list
            mm = int(split_s_slash[0])
            dd = int(split_s_slash[1])
            yyyy = int(split_s_slash[2])
        except:
            raise syntax_message            #raising error message when error is occured
        check_number(mm, 'Month', 1, 12)    #putting month in the check_number function so that I can check if it is valid
        check_number(dd, 'Day', 1, 31)      #                      "
        check_number(yyyy, 'Year', 1900, 2021) #                   "
        return (int(mm),int(dd),int(yyyy))     #if it is finally checked as valid value, return them in proper tuple format

    elif len(split_s_dash) == 3:                                                                        #repeating the same process in dash-splitted case as well
        if len(split_s_dash[0]) != 2 and len(split_s_dash[1]) != 2 and len(split_s_dash[2]) != 4:
            raise syntax_message
        try:
            mm = int(split_s_dash[0])
            dd = int(split_s_dash[1])
            yyyy = int(split_s_dash[2])

        except:
            raise syntax_message
        check_number(mm, 'Month', 1, 12)
        check_number(dd, 'Day', 1, 31)
        check_number(yyyy, 'Year', 1900, 2021)
        return (int(mm),int(dd),int(yyyy))
    else:
        raise syntax_message
    
    

        

if __name__ == '__main__':
    while True:
        try:
            s = input("Input a date: ")
            if s and s[0] == 'q':  # quit
                break
            print(parse_date(s))
        except SyntaxError as e:
            print(e)
            pass
        except ValueError as e:
            print(e)
            pass

### Problem 2

import math

class stack:
    def __init__(self):
        self.s = []

    def pop(self):
        top = self.s[0]
        self.s = self.s[1:]
        return top

    def push(self,item):
        self.s = [item] + self.s

    def empty(self):
        return self.s == []

    def peek(self):
        return self.s[0] if len(self.s) else None
        
    def __str__(self):
        return str(self.s)
        
class calc:
    def __init__(self):
        self.s = stack()

    def _op1(self,f):
        """ 
        Args:
        self (instance of class)
        f (function)

        Returns:
        function output (integer or float)
        OR error message (string)
        """
        # f is a function that takes one operand
        # apply f to top item in stack.  
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on

        
        try:
            x = self.s.pop()    #defining popped value of x
            self.s.push(f(x))   #trying push(f(x)) in stack class
            return f(x)         #if it is valid, returns f(x) result
        except Exception as e:
            self.s.push(x)      #restoring error casuing operand
            raise e             #if it is not valid, raises error message e
            


    def _op2(self,f):
        """ 
        Args:
        self (instance of class)
        f (function)

        Returns:
        function output (integer of float)
        OR error message (string)
        
        """
        # f is a function that takes two operands
        # apply f to top two items in stack.  top 
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        xy = []                         #making empty list to append

        try:
            xy.append(self.s.pop())     #appending first value
            xy.append(self.s.pop())     #appending second vlaue
            self.s.push(f(xy[0],xy[1])) #pushing both values appended in the xy list
            return f(xy[0],xy[1])       #if they are valid, returns the result
        except Exception as e:
            for i in xy[::-1]:              #reading reversely
                self.s.push(i)              #restoring error causing operands
            raise e                         #if it is not valid, raises the error message e


    def clear(self):
        """ 
        Args:
        self (instance of class)
        """
        # clear the stack 
        self.s = stack()        #restarting the class

    def e(self):
        """ 
        Args:
        self (instance of class)
        """
        # push math.e on stack

        self.push(math.e)           #pushing exponential constant


    def ln(self):
        """ 
        Args:
        self (instance of class)
        """
        # compute math.log(top of stack) (see math module)
        # use _op1
        return self._op1(lambda x: math.log(x))     #defining ln(x) with _op1 function

    def add(self):
        """ 
        Args:
        self (instance of class)
        """
        # add top two elements on stack 
        # use _op2 
        # return top element or exception

        return self._op2(lambda x, y : y+x)         #defining addition with _op2 fnction

    def div(self):
        """ 
        Args:
        self (instance of class)
        """
        # divide top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y : y/x)         #defining division with _op2 function

    def mult(self):
        """ 
        Args:
        self (instance of class)
        """
        # multiply top two elements on stack 
        # use _op2
        # return top element or exception
        return self._op2(lambda x, y : y*x)         #defining multiplication with _op2 function

    def minus(self):
        """ 
        Args:
        self (instance of class)
        """
        # subtract top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y : y-x)         #defining subtraction with _op2 function

    def exp(self):
        """ 
        Args:
        self (instance of class)
        """
        # compute x**y with top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y : y**x)        #defining exponent calculation with _op2 function
    
    def push(self,data):
        """ 
        Args:
        self (instance of class)
        data (string)
        """
        # push float(data) onto stack
        try:
            self.s.push(float(data))                #trying to push the data as float
        except:
            raise ValueError('could not convert string to float: '+"'"+data+"'")     #if it is not convertible, raises the error message

    def work(self,data):
        try:
            if data == 'c':
                self.clear()
                return "Starting new computation"
            elif data == 'e':
                return str(self.e())
            elif data == 'ln':
                return str(self.ln())
            elif data == '+':
                return str(self.add())
            elif data == '-':
                return str(self.minus())
            elif data == '*':
                return str(self.mult())
            elif data == '/':
                return str(self.div())
            elif data == '^':
                return str(self.exp())
            else:
                str(self.push(data))
        except Exception as e:
            return str(e)
    
    def __str__(self):
        return str(self.s)

if __name__ == "__main__":
    i = 0
    w = calc()
    while True:
        # uncomment the following to help debugging
        #print(w)
        data = input(f"{i}: ").strip()
        if data == 'q':
            print('Terminated')
            break
        else:
            result = w.work(data)
            if result != None:
                print(result)
        i = 0 if data == 'c' else i+1   