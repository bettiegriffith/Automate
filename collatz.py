import sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1

    while result == 1:
        print(result)
        sys.exit()

    while result != 1:
        print(result)
        number = result
        return collatz(number)

print('Enter a number: ')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('Please enter an integer.')
