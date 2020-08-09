def calculate_factorial(num):
    if (num == 0):
        return 1
    else:
        return num * calculate_factorial(num - 1)


print(calculate_factorial(5))
