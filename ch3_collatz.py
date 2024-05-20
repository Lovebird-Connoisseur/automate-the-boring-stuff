def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * int(number) + 1

try:
    number = int(input('Number: '))

    collatz(number)

    while collatz(number) != 1:
        print(collatz(number))
        number = collatz(number)
    else:
        print(collatz(number))

    number = collatz

except ValueError:
    print("Invalid value! Value Must be a whole number!")
