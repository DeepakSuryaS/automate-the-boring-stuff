# The following code explains the optional parameters of the print()

print('Hello')
print('World') # the output will be on different lines by default because print() adds a newline character to the end of the string it is passed.

# setting the end keyword argument to a different string
print('Hello', end='') # end is an empty string rather than the newline character
print('World') # both the words will be in the same line with no separator

# sep parameter
print('cats', 'dogs', 'mice')
# output will be separated by spaces by default

# setting the sep keyword argument to a different value
print('cats', 'dogs', 'mice', sep=', ')
