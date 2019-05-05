# This program says hello and asks for my name

print("Hi there!")
print("What's your name?") # asks for name
myName = input() # gets the input and saves it in myName variable
print("It's so nice to meet you, " + myName + ".")
print("Your name is " + str(len(myName)) + " characters long.") # calculates the length of the name
print("How old are ya?") # asks age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year. Cool!")

