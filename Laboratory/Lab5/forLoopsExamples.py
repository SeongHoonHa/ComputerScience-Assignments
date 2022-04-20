# Use case 1: When you simply need to visit each element in a collection of things for ex. 
# in a list - Use the simple for loops with the 'in' keyowrd. You don't need to use 'range' function.

example_list_1 = [3, 4, "nice work", 90.9876, 0, '*', '_']

# Printing every element of the example_list_1
for item in example_list_1:
  print(item)


# Use case 2: more often, we want to do some processing on the elements in our 
# list rather than just printing them. For example, you want to answer questions 
# like - print the element if it's a string or an integer.  In this case, you use the 
# IF/ELSE structure inside the loop to test the type of the element.

print("\n")
for item in example_list_1:
  if type(item) == str:
    print(item)


# Use case 3: What if you get a list of lists! 
# Let's see what happens in this case. Tell the students how the 'item' now prints the sublists.

example_list_2 = [[0,1,2], ["A", "B"], ['$', '#', '*'], "Hello", [], []]

print("\n")
# The following loop will simply visit each element inside the list - no different then previous example only that our list now contains sublists!
for item in example_list_2:
  print(item)



# Use case 4: What if you now want to do something with the sublists? 
# Let's say we want to print the second element from our sublists.
# We will need to two things now,

#  -1) We will need to check if the item that we get is indeed a sublist (and not an integer or a string) because only a sublist (which is also a list) will have the 2nd element that we want to print. If it's an integer or a string then basically you don't have any second element because the integer is the only thing that you have. Also we will need to check that the sublist is not empty because we can't access anything inside an empty sublist.

# - 2) If item is indeed a list then we will need to index the second element from our sublist and then print it.

# - This requires us to use `if` conditional and list indexing inside the for loop.

print("\n")
for item in example_list_2:
  if len(item)>1 and type(item) == list: # <-- non-empty list (not an integer/string/float) and that the list have atleast 2 elements.
    print(item[1]) # <-- Index the 2nd element and print it.