### 11 / 22 / 2020
### Author: Elijah Oleary
### How to Edit Lists


# Creating a list of months
birthday_months = ['april', 'may', 'november']

# Printing our list
print(birthday_months)

# Chaning an element of list
birthday_months[0] = 'april'

print(birthday_months)

# Using the .append method
birthday_months.append('june')

print(birthday_months)

# Creating an empty list
birthday_months = []

print(birthday_months)

birthday_months.append('august')

print(birthday_months)

# Using the .insert method
birthday_months.insert(0, 'may')

print(birthday_months)

# Using the delete method
del birthday_months[1]

print(birthday_months)