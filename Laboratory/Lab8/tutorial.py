# Code from Lab 8, here for your reference

def main():
    #############################################
    # ternary operators
    #############################################
    print("Even" if 5 % 2 == 0 else "Odd")
    # Should give: 'Odd'
    
    print("Even" if 8 % 2 == 0 else "Odd")
    # Should give: 'Even'

    #############################################
    # list comprehensions
    #############################################
    print([2*i for i in range(4)])
    # Should give: [0, 2, 4, 6]
    
    # We can do multiple for-loops
    print([(i,j) for i in range(4) for j in range(3)])
    # Should give: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
    
    # We can also filter the results by an if-statement at the end:
    print([i for i in range(10) if i % 3 == 0])
    # Should give: [0, 3, 6, 9]


    #############################################
    # lambda expressions
    #############################################
    print((lambda x: x**2)(5))
    # Should give: 25

    # We can also have multiple parameters
    print((lambda x, y, z: x**2 + 2*y - z)(5, 6, 7))
    # Should give: 30


    #############################################
    # map
    #############################################
    print(list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    # Should give: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    #############################################
    # filter
    #############################################
    print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    # Should give: [3, 6, 9]

    #############################################
    # reduce
    #############################################
    from functools import reduce
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # Should give: 55

if __name__ == "__main__":
    main()