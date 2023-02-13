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

# String Methods
language ='$Python$$'
message = 'I love Python!'

# YOUR CODE STARTS HERE:
language1 = language.strip('$')
language2 = language1.lower()
message1 = message.upper()
message2 = message.replace('Python', 'Java')
print(language2 + " " + language1 + " " + message2 + " " + message1)

# Challenges
# 1
my_str1 = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
new_add = my_str1[32::]
print("  ", new_add)

# 2
#  "You've got an error!"
# \n means a new line.
# \ is known as the escape character.
print("You've got an error! \n \\n means a new line. \n \ is known as the escape character.")

# Write a Python script that converts foot[ft] to centimeter[cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.
xy = float(input("enter a value in foot   \n"))
xy = xy * 30.48
print(f"the value is {xy:.2f} cm")

# Challenge #4
# Write a Python script that tests if a string is a palindrome.
yx = "madam"
print(f"is palindrome? {yx == yx[::-1]}")

# Challenge 5
yx = yx.replace(" ", "").lower()
print(f"is palindrome? {yx == yx[::-1]}")

# Challenge 6
abc = input("Enter a string of atleast characters\n")
n_abc = abc[:2] + abc[-2:]
print(n_abc)

# challenge 7
cde = input("Enter a string\n")
z = cde[0]
n_cde = cde[1:].replace(z, "$")
cde1 = z + n_cde
print(cde1)
# Challenge 8

n = int(input("enter an integer"))
my_str = input(" Enter a string")
f_line = my_str[:n]
l_line = my_str[n+1:]
new_line = f_line + l_line
print(new_line)

# challenge 9
my_even = input('Enter the string to change:')
new_str = my_even[::2]
print(new_str)
# 10
rad = float(input('Enter circle radius:'))
area = 3.1415 * rad ** 2
print(f'The area of a circle with a radius of {rad} is {area:.4f}')
