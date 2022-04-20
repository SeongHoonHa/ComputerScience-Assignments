class MyFraction:
    """
    This class allows for the representation of fractions.
    """

    def __init__(self, numerator, denominator):
        """
        This class will make a fraction:
               numerator 
        ---------------------------
              denominator
        """
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        """
        This function will return the fraction evaluated into a decimal
        """
        return self.numerator/self.denominator

    def __add__(self, other):
        """
        Adds 2 fractions together. 
        Handles addition by making the denominators the same.
        a   c           ad + cb
        - + -    <-->   -------
        b   d             bd
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return MyFraction(a*d+c*b, b*d)

    def __sub__(self, other):
        """
        Subtracts 2 fractions. 
        Handles addition by making the denominators the same.
        a   c           ad - cb
        - - -    <-->   -------
        b   d             bd
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return MyFraction(a*d-c*b, b*d)

    def __mul__(self, other):
        """
        Multiplies 2 fractions. 
        a   c           a*c
        - * -    <-->   ---
        b   d           b*d
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return MyFraction(a*c, b*d)
    def __str__(self):
        """
        Makes a fraction representation
        Example:
        f = 4/5
        """
        return f"f={self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        Compare two instance of Fraction to see if they are equal.
        Here we check that the parts are equal rather than using evaluate()
        to demonstrate how you might do this without the 'float' type.
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return a*d == c*b

    def __lt__(self, other):
        """
        Compare two instance of Fraction to see if one is less than the other.
        a   b         
        - < -    <-->   ad < bc
        b   c
        if b, d share the same sign, and is

                 <-->   ad > bc
        if b, d have opposite signs.
        
        For more information, see:
            https://math.stackexchange.com/questions/2979431/does-cross-multiply-always-work-for-inequalities-if-both-denominators-are-both-p
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator    
        if b*d > 0 :
            return a*d < b*c
        else:
            return a*d > b*c

    def __le__(self, other):
        """
        Compare two instance of Fraction to see if one is less than or equal the other.
        Note that you can conveniently make use of __lt__ and __eq__
        """
        return (self < other) or (self == other)

    def __gt__(self, other):
        """
        Compare two instance of Fraction to see if one is greater than the other
        Note that you can conveniently make use of __le__
        """
        return not (self <= other) 

    def __ge__(self, other):
        """
        Compare two instance of Fraction to see if one is greater than or equal the other
        Note that you can conveniently make use of __lt__
        """
        return not (self < other)
