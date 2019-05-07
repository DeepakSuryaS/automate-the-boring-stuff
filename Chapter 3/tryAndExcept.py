# Error handling

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
# print(spam(0)) # causes divide by zero error and prevents the rest of the program from executing
print(spam(1))

# try and except

def spamNew(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Can't divide by zero bruh.")

print(spamNew(2))
print(spamNew(12))
print(spamNew(0))
print(spamNew(1))

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) # this will not be executed because the previous will cause an error and move the execution to the except clause and it doesn't come back to the try clause. Instead, it just continues to move down as normal.
except ZeroDivisionError:
    print('Error: Invalid argument.')
