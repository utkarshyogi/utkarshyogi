# Approach 1
# def factorial(target):
#     if target > 0:
#         return target * factorial(target-1)
#     return 1
#print(factorial(5))


# Approach 2
def fac (num, mult):
    if num > 0:
        fac(num-1,mult*num)
    else:
        print(mult)


fac(5,1)
