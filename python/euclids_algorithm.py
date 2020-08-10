def get_greatest_common_divider(num1, num2):
    while num1 != 0 and num2 != 0:
        if (num1 > num2):
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


print(get_greatest_common_divider(100, 10))


# in python module math exist function gcd(a,b)
