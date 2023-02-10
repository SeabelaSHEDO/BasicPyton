# Strings
# create a variable info1 that stores the string: 'Jonathan' is an apple variety and "Chardonnay" is a grape variety

info1 = "'Jonathan' is an apple variety and \"Chardonnay\" is a grape variety"


# create a variable info2 that stores the string: \n is a newline escape sequence
info2 = '\\n is a newline escape sequence'


# Converting types
a = '1.5'
b = '2'
# Using Type Casting create a new variable called c
# that stores the result of a multiplied by b. c stores a float and will be 3.0.
c = float(a) * float(b)
print(c)

# String Indexing and operations
my_str = 'Python is TIOBE language of the year 2023!'

# define a variable named s1 that stores the
# character T from the string above. Use a positive index to get the character T
s1 = my_str[10]


# define a variable named s2 that stores the character 8 from
# the string above. Use a negative index the get the character 3
s2 = my_str[-2]
s3 = s1 + s2
# concatenate s1 and s2 in a new variable called s3. s3 will store the string T3
print(s3)



my_str = 'eth0:192.168.122.1'

# YOUR CODE STARTS HERE
# using string slicing, create a variable called my_interface
# that stores the substring 'eth0'
my_interface = my_str[0:4]
print(my_interface)

digits = '0123456789'
# #YOUR CODE STARTS HERE
# using string slicing, create a variable called x
# that stores the substring '9630'
x = digits[::-3]
print(x)
