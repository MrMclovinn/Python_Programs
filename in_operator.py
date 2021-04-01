### 03 / 26 / 2021
### ELijah Oleary
### Using a key to get a value

# Create a dictionary of terms
terms = {}

terms['variable'] = 'Represents or refers to a value stored in memory'
terms['integer'] = 'A whole number.'

print(terms['variable'])
print(terms['integer'])

# Or

Terms = {'variable' : 'Represents or refers to a value stored in memory', 'string' : 'A sequence of characters'}

if 'float' in Terms:
    print("I know what a float is")
else:
    print('I do not know what that is')
print(Terms['variable'])