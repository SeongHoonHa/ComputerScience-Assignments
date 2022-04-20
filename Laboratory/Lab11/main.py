from Fraction import MyFraction

def insertion_sort(xlist):
    """
    Gets a list and returns a sorted list using Insertion Sort

    Note that the list can consist of any object with __lt__ defined.  
    This includes, for example, MyFraction instances.
    """
    # Traverse through 1 to len(xlist)
    for i in range(1, len(xlist)):
  
        key = xlist[i]
  
        # Move elements of xlist[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < xlist[j] :
                xlist[j+1] = xlist[j]
                j -= 1
        xlist[j+1] = key
    return xlist
  
  
def partition(xlist, low, high):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in the sorted
    list, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot.

    Note that the list can consist of any object with __le__ defined.  
    This includes, for example, MyFraction instances.    
    """
    i = (low-1)         # index of smaller element
    pivot = xlist[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if xlist[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            xlist[i], xlist[j] = xlist[j], xlist[i]
  
    xlist[i+1], xlist[high] = xlist[high], xlist[i+1]
    return (i+1)
  

def quickSort(xlist, low, high):
    """
    Gets a list and returns a sorted list using Quick Sort

    Note that the list can consist of any object with __lt__ defined.  
    This includes, for example, MyFraction instances.

    Input:
        xlist[] --> List to be sorted,
        low  --> Starting index,
        high  --> Ending index
    Returns:
        The sorted list
    """
    if len(xlist) == 1:
        return xlist
    if low < high:
  
        # pi is partitioning index, xlist[p] is now
        # at right place
        pi = partition(xlist, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(xlist, low, pi-1)
        quickSort(xlist, pi+1, high)
  
def binary_search(xlist, low, high, x):
    """
    Function to do binary search.

    Returns index of x in xlist if present, else -1

    Note that the list can consist of any object with __gt__ and
    __ge__ defined.  This includes, for example, MyFraction instances.
    """
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if xlist[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left sublist
        elif xlist[mid] > x:
            return binary_search(xlist, low, mid - 1, x)
 
        # Else the element can only be present in right sublist
        else:
            return binary_search(xlist, mid + 1, high, x)
 
    else:
        # Element is not present in the list
        return -1


if __name__ == "__main__":
    f1 = MyFraction(1, 2)
    f2 = MyFraction(3, 10)
    f3 = MyFraction(7, 12)
    f4 = MyFraction(2,20)

    five3 = MyFraction(5,3)
    five2 = MyFraction(5,2)
    two5 = MyFraction(2,5)

    # testing evaluate
    print()
    print("~~~TESTING EVALUATE~~~")
    print("Proper  | Your Solution")
    print("------------------------")
    print(f"{1/2:.4f}  | {f1.evaluate():.4f} ")
    print(f"{3/10:.4f}  | {f2.evaluate():.4f} ")
    print(f"{7/12:.4f}  | {f3.evaluate():.4f} ")
    print(f"{2/20:.4f}  | {f4.evaluate():.4f} ")

    # testing add
    print()
    print("~~~TESTING ADD~~~")
    print("Proper | Your Solution")
    print(f"16/20 | {f1 + f2}")
    print(f"164/240 | {f3 + f4}")

    # testing sub
    print()
    print("~~~TESTING SUB~~~")
    print("Proper    | Your Solution")
    print(f"16/40     | {f1 - f4}")
    print(f"-34/120 | {f2 - f3}")

    # testing ==, <, <=, >, >=
    l = [f1, f2, f3, f4]
    print()
    print("~~~TESTING Inequalities~~~")
    print("Ineq        | Proper   | Your Solution")
    print(f"5/3==5/3    | True     | {five3 == five3}")
    print(f"5/2==2/5    | False    | {five3 == two5}")

    print(f"5/3 < 5/3   | False    | {five3 < five3}")
    print(f"5/3 < 5/2   | True     | {five3 < five2}")
    print(f"5/2 < 5/3   | False    | {five2 < five3}")

    print(f"5/3 <= 5/3  | True     | {five3 <= five3}")
    print(f"5/3 <= 5/2  | True     | {five3 <= five2}")
    print(f"5/2 <= 5/3  | False    | {five2 <= five3}")

    print(f"5/3 > 5/3   | False    | {five3 > five3}")
    print(f"5/3 > 5/2   | False    | {five3 > five2}")
    print(f"5/2 > 5/3   | True     | {five2 > five3}")

    print(f"5/3 >= 5/3  | True     | {five3 >= five3}")
    print(f"5/3 >= 5/2  | False    | {five3 >= five2}")
    print(f"5/2 >= 5/3  | True     | {five2 >= five3}")


    l = [f1, f2, f3, f4]
    print()
    print("~~~TESTING Insertion Sort~~~")
    sorted_list = insertion_sort(l)
    for i in sorted_list:
        print(i)

    l = [f1, f2, f3, f4]
    print()
    print("~~~TESTING Quick Sort~~~")
    quickSort(l, 0, len(l)-1)
    for i in l:
        print(i)

    print()
    print("~~~TESTING Binary Search~~~")
    index = binary_search(l, 0, len(l)-1, f2)
    print(index)
   