def collatz_conjecture(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        iterations += 1
        number = int(number)
    return iterations


def collatz_max(min_n, max_n):
    # iterate into a list that holds values of collatz_conjecture
    # max +1 to include last number
    collatz_list = [collatz_conjecture(i) for i in range(min_n, max_n + 1)]

        # returns number with highest chain and the amount of chains
        # get the index of the max of the list and add the min range to
    return collatz_list.index(max(collatz_list)) + min_n, max(collatz_list)


# inputs min and max
# outputs (max_chain_number, chain_count)
print(collatz_max(2, 30))

