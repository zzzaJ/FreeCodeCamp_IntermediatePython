# Lists
# Ordered, Mutable, Allows duplicate elements

a_list = ["banana", "cherry", "apple"]

# Use list object type to create a new list
empty_list = list()

different_types = [1, False, "A_LIST"]

item = different_types[1] # This will return False, as it is the second item in the list starting from index 0
item2 = different_types[-1] # This refers to the last item in the list ("A_LIST")
item3 = different_types[-2] # This refers to the second last item in the list (False)

# To iterate over a list:
for x in different_types:
    print(x)

# Check in list
if "banana" in a_list:
    print("yes")
else:
    print("no")

# Check the length of a list
len(different_types)

# Append items
different_types.append("True!")

# Insert item at specific index
different_types.insert(1, "1234")

# Remove item (returns the last item and removes it)
different_types.pop()

# Remove specific item using .remove
# Will throw error if not in list, and will only return and remove the first instance
different_types.remove("1234")

# Reverse the list
different_types.reverse()

# Sort the list 
# This sorts in place, so will change order of the original list
different_types.sort()

# To return a sorted list, use sorted()
new_list = sorted(different_types)

# Create new list with the same elements
zero_list = [0] * 5

# Concatenate lists
another = new_list + zero_list

# Slicing lists
my_list = [1,2,3,4,5,6,7,8,9]

# Slice a list

# use list[a:b]
# Where a is the first index to be included, up until and excluding the index b
# If no start specified, it starts from 0
# If no stop is specified, it ends at len(list)
a = my_list[1:5] # returns [2,3,4,5]

# to change steps between items use
# use list[a:b:s]
# a is the start index, b is the exclusive end index, and s is the step inbetween..
b = my_list[1::2] # This will return [2,4,6,8]... Go from index 1 to index end, with step of 2

# A negative step can also be used
# to reverse the list
c = my_list[::-1] # returns [9,8,7,6,5,4,3,2,1]

# Copying a list
ori = ["banana", "cherry", "apple"]

# NOT A COPY!
copy = ori # This is not a copy! Both refer to the same reference in memory

copy = ori.copy() # This will create a deep/shallow? copy of the object

# Both of these methods below will also perform a shallow copy.. NB Deep copy since strings are immutable in python
copy = list(ori)
copy = ori[::1]


# List comprehension
# Creating new lists from exisiting lists in 1 line

a_list_2 = [1,2,3,4,5,6,7,8]
b = [i*i for i in a_list_2] # returns a list where each item is squared from an existing list

# Synax:
# new_list = [ (opperation using reference) for (reference) in (original_list) ]
