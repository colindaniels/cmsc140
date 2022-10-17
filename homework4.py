# Q1: Indexing

a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))

def listdiff(lst1, lst2):
    return [i for i, _ in enumerate(lst1) if lst1[i] != lst2[i]]

diff = listdiff(a, b) # this shouldn't print anything
print(diff) # this should print [8, 15, 16, 19]


# Q2: Schedule Saver