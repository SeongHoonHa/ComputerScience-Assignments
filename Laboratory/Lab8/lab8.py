
def zero_every_other(xlist):
    """
    Function to zero out every other element of a list,
    starting from the first element.

    Example:
    >>> zero_every_other([1, 2, 3, 4, 5])
    [0, 2, 0, 4, 0]
    """
    for i in range(len(xlist)):
        if i % 2 == 0:
            xlist[i] = 0
    return xlist

def zero_every_other_comp(xlist):
    """
    Rewrite zero_every_other using a list comprehension
    """
    return [0 if i % 2 == 0 else xlist[i] for i in range(len(xlist))]
    # return [xlist[i] if i % 2 != 0 else 0 for i in range(len(xlist))]

def zero_every_other_mapfilter(xlist):
    """
    Rewrite zero_every_other using map, lambdas
    (Do *not* use list comprehensions!)
    Remember to convert your final value into a list using list()!

    For simplicity, you can assume that all elements of xlist are distinct.
    Challenge:  How would you do this without this assumption?
    """
    return list(map(lambda x: 0 if xlist.index(x) % 2 == 0 else x, xlist))
    #return list(map(lambda i: 0 if i%2 == 0 else xlist[i], range(len(xlist))))


if __name__ == "__main__":
    print("****************************")
    print("* TESTING ZERO_EVERY_OTHER *")
    print("****************************")
    #tests = [([1, 2, 3, 4, 5], [0, 2, 0, 4, 0])]
    funcs=[zero_every_other,zero_every_other_comp,zero_every_other_mapfilter]
    for i in range(3):
        xlist=[1,2,3,4,5]
        expected=[0,2,0,4,0]
        print("\n")
        print("function {}\n".format(i+1))
        print("---------------\n")
        print("Your output: \n")
        print(funcs[i](xlist))
        print("Expected output: \n")
        print(expected)
