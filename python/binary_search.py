def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while(low <= high):
        middle = (low + high) // 2
        guess = list[middle]
        if(guess < item):
            low = middle + 1
            print(f"Number > then  {guess}, range = {low}-{high}")
        elif(guess > item):
            high = middle - 1
            print(f"Number < then  {guess}, range = {low}-{high}")
        else:
            print(f"Number was found - {guess}")
            return middle


my_list = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]
binary_search(my_list, 1)
