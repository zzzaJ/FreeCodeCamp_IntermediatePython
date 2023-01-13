# Tuples
# Ordered, immutable, allows duplicate elements
# Often used for objects that belong together

my_tuple = ("Max", 28, "Boston")
same_tuple = "Max", 28, "Boston"

# NB a tuple with a single element will be recognised as the data type
# This will be a string
a_str = ("string")
# This will be a tuple with a single string in it
a_str_tuple = ("string",)

# We can also construct using the tuple class, passing in an iterable (or array)
a_tuple = tuple(["Max", 28, "Boston"])

# Retrieve an item
# This will return "Max"
item = a_tuple[0]

# This will return "Boston", the last element
item = a_tuple[-1]

# Adding an element will result in an error
a_tuple[3] = "ERROR"

# Iterating over tuple elements
for x in a_tuple:
    print(x)

# Check contains
if "Max" in a_tuple:
    print("yes")
else:
    print("no")

# Get length
len(a_tuple)

# Count occurances of element in tuple
# This will return 1
a_tuple.count("Max")

# Get first index of specific element
# This will return 1
a_tuple.index(28)

# This will return an error
a_tuple.index("Not There")

# Convert tuples to list, and back
my_list = list(1,2,3,4,5)
a_tuple_list = tuple(my_list)
my_list = tuple(my_list)

# Slicing tuples
b = (1,2,3,4,5,6,7,8,9,10)
# Slicing tuple b, from index 2 up until (excluding) index 5
# So this will return (3,4,5)
new_b = b[2:5]

# Without a start index, it will defualt to 0
# Without a stop index, it will default to len(the_tuple)

# We can also use a step arguement
# This will return (1,3,5,7,9)
new_step_b = b[::2]

# Using a negative step will reverse it (like lists)
# This will return (10,9,8,7,6,5,4,3,2,1)
rev_b = b[::-1]

# Unpacking a tuple
a = ("Max", 28, "Boston")

# We an unpack a tuple into various variables
# name = Max, age = 28, city = Boston
name, age, city = a

# However, unequal vars and tuple length with error
# This will throw an error
name, age, city, error = a

# We can unpack multiple elements with a *
z = (0,1,2,3,4)

# We specify vars to assign tuple values to
# Using a * before the one which will contain more than 1 tuple element
# This will return
# i1 = 0, i2 = [1,2,3], i3 = 4
i1, *i2, i3 = z

# Tuples can be more efficient than lists, since they are immutable
# This shows that they take up less space in mem
import sys
tpl = (0,1,2,"hello",True)
lst = [0,1,2, "hello", True]
sys.getsizeof(tpl)
sys.getsizeof(lst)

# They can also be more efficient to iterate over, and to create them
# This shows that creating tuples is much faster than creating lists
# Timeit will show time to do stmt opperation number number of times.
import timeit
timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)
timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)