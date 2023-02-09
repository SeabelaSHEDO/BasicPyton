import math
# FIRST CODING ACTIVITY

# define variable called sold and set it to any boolean value
product_name = "Coke"

# define a variable named quantity and set it to any integer
quantity = 10

# define a variable called price and set it to any float
price = 23.90

# define variable called sold and set it to any boolean value
sold = False

# ACTIVITY 2
# Using Python Math Operators create the following variables:
#
#     c equals a divided by b
#
#     d equals a raised to the power of b
#
#     e equals the remainder of a divided by b
#
#     f equals a multiplied by b

a = 9
b = 2

# YOUR CODE GOES HERE:
c = a / b
d = a ** b
e = a % b
f = a * b

# ACTIVITY 3
#
# ## YOUR CODE STARTS HERE. Replace None with the correct formula!
#
# ## The distance from LA to NYC in miles
# distance_miles = 2806
# ## Distance in Km. 1 mile = 1.609 km
# distance_km = None
#
#
# ## Temperature in degrees Celsius
# temperature_c = 25
# The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32
# ## Temperature in Fahrenheit
# temperature_f = None
#
# ## Size in inch
# inch = 17
# ## 1 inch is equal to 2.54 centimeters
# ## Size in cm
# cm = None
#
# ## 1 Year has 365 days, 1 day has 24h, 1h has 3600 sec
# year_in_seconds = None

# YOUR CODE STARTS HERE. Replace None with the correct formula!

# The distance from LA to NYC in miles
distance_miles = 2806
# Distance in Km. 1 mile = 1.609 km
distance_km = distance_miles * 1.609


# Temperature in degrees Celsius
temperature_c = 25
# The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32
# Temperature in Fahrenheit
temperature_f = 25 * (9 / 5) + 32

# Size in inch
inch = 17
# 1 inch is equal to 2.54 centimeters
# Size in cm
cm = inch * 2.54

# 1 Year has 365 days, 1 day has 24h, 1h has 3600 sec
year_in_seconds = 365 * 24 * 3600

# Python_Basic Challenges
# One
aa, bb, cc, dd = 2, 1.3, False, 'Hello world'
print(type(aa), aa, " ")
print(type(bb), bb, " ")
print(type(cc), cc, " ")
print(type(dd), dd, " ")

# Two
my_name = 'Andrei'
value = 100


# This is
# an example of a multiline
# comment in Python.


star = 'Hello'
print(star)

# Three
# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne'
print('My best friend is ', best_friend)

age = 18
print(age)

a, b = '10', '20'
print(a + b)

print('To comment a line of code you # at the beginning of the line.')

# four
# Create a new Python script that uses the following operators:
# =, ==, >=, *, **, /, //, %, +=, *=

y, z = 5, 7
x = 12
print(x == y + z)
print(x >= y)
print(y * z)
print(z ** 1)
print(x / y)
print(x // z)
print(z % y)
y += 1
print(y)
z *= 2
print(z)
print("    ")

# Five
# Consider
# the
# following
# Python
# expression: a = 16 / 2 + 6 / 2 ** 2
#
# Add
# parenthesis
# to
# change
# the
# order
# of
# operations
# so
# that
# an is 1.0

change = (16 / (2 + 6) / 2) ** 2
print(change)

# SIX
# An IPv6 address is represented using 128 bits.
#
# Write a Python script
# that calculates how many IPv6 addresses are available.
# You can also include reserved IP address.

ipv6_adr_no = 2 ** 128
print(ipv6_adr_no)

# SEVEN

# A company 's revenue is 45,897,513. Calculate the company
# 's profit if the profit represents 12.7% of the revenue. ' \
# 'Display the profit using 2 decimal places.
profit = 0.127 * 45_897_513
print(round(profit, 2))
print("  ")

# Eight

a = 0.1
b = 0.3
print(math.isclose(a * 3, b))  # => False
