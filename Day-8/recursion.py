""" Q1. """
# # factorial of a number
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fact(n-1)*n


# print(fact(4))

""" Q.2 """
# fibonna series
# 0 1 1 2 3 5 8


# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)


# for i in range(5):
#     print(fibo(i))

""" Calculate GCD of 2 numbers"""


# def gdc(a, b):
#     # given a is greater than a
#     while b:
#         a, b = b, a % b
#     return a


# print(gdc(25, 15))

""" Q3. Sum of digit"""
# num = int(input("Enter number to add"))


# def add(n):
#     if n == 0:
#         return 0
#     rem = n % 10
#     ans = add(n // 10)
#     return ans+rem


# print(add(846210))

""" Q.4 revese a string using recursion """


def rev(s):
    if len(s) == 1:
        return s
    firele = s[0]
    ans = rev(s[1:])
    return ans+firele


print(rev("hello"))
