def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

def caller():
    try:
        num = int(input('Give me a number: '))
        while num != 1:
            num = collatz(num)
    except ValueError:
        print('Ooh, my common sense is tickling! STFU and enter an integer idiot.')
        caller()

caller()
