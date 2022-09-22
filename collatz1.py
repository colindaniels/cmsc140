def collatz_conjecture(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        iterations += 1
        number = int(number)
        print(number)
    return iterations


# outputs chain count
print(collatz_conjecture(20))
