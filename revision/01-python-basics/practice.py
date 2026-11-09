"""
Day 1 of revision: basic Python programs.

How to use:
  1. Write your code inside each function, replacing the `pass` line.
  2. Run:  python revision/01-python-basics/practice.py
  3. Each function prints PASS or FAIL. Patterns are printed so you can check them by eye.

Rules: try without slicing tricks like s[::-1] first, then write the short version too.
"""

# ---------------- A. Reverse ----------------


def reverse_string(s: str) -> str:
    """'hello' -> 'olleh'. Use a loop or two pointers, not s[::-1]."""
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev


def reverse_string_recursive(s: str) -> str:
    """Same thing, but with recursion. Watch the base case for '' (empty string)."""
    if s == "":
        return s
    return reverse_string_recursive(s[1:]) + s[0]


""" same like rev = rev + ch  same analogy """


def reverse_number(n: int) -> int:
    """1234 -> 4321, -120 -> -21. Use % and // only (no str())."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while (n):
        dig = n % 10
        rev = rev*10 + dig
        n = n//10
    return sign*rev


def is_palindrome(s: str) -> bool:
    """'racecar' -> True, 'hello' -> False. Use two pointers."""
    n = len(s)
    low = 0
    high = n-1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


# ---------------- B. Factorial & friends ----------------

def factorial_loop(n: int) -> int:
    """5 -> 120, 0 -> 1."""
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return factorial_recursive(n-1)*n


def fibonacci(n: int) -> list:
    """Return the first n Fibonacci numbers: 7 -> [0, 1, 1, 2, 3, 5, 8]."""
    # list1 = []
    # for i in range(n):
    #     def fibo(i):
    #             if i== 1 or i==0:
    #                 list1.append(i)
    #             list1.append(fibo(i-1)+fibo(i-2))
    # return list1
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result


def sum_of_digits(n: int) -> int:
    """846210 -> 21."""
    temp = n
    sum = 0
    while temp:
        dig = temp % 10
        sum += dig
        temp = temp // 10
    return sum


def is_prime(n: int) -> bool:
    """Check divisors only up to sqrt(n)."""
    pass


def gcd(a: int, b: int) -> int:
    """Euclid's algorithm: gcd(25, 15) -> 5."""
    while b:
        a, b = b, a % b
    return a


# ---------------- C. Patterns (print them) ----------------
# Example for n = 4 is shown in each docstring.

def right_triangle(n: int):
    """
    *
    * *
    * * *
    * * * *
    """
    for i in range(1, n+1):
        print("*")


def inverted_triangle(n: int):
    """
    * * * *
    * * *
    * *
    *
    """
    for i in range(n):
        print("*" * n-i)


def pyramid(n: int):
    """
       *
      ***
     *****
    *******
    """
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


def number_triangle(n: int):
    """
    1
    1 2
    1 2 3
    1 2 3 4
    """
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")


def floyd_triangle(n: int):
    """
    1
    2 3
    4 5 6
    7 8 9 10
    """
    count = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(count, end=" ")
            count += 1
        print()


def diamond(n: int):
    """
       *
      ***
     *****
    *******
     *****
      ***
       *
    """
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # bottom half: the same formula, i counting down n-2 .. 0
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


# ---------------- tests (don't edit below) ----------------

def _check(name, got, expected):
    status = "PASS" if got == expected else "FAIL"
    extra = "" if status == "PASS" else f"   got {got!r}, expected {expected!r}"
    print(f"[{status}] {name}{extra}")


def _run(name, fn, *cases):
    for args, expected in cases:
        try:
            _check(f"{name}{args}", fn(*args), expected)
        except Exception as e:
            print(f"[FAIL] {name}{args}   raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("--- A. Reverse ---")
    _run("reverse_string", reverse_string,
         (("hello",), "olleh"), (("",), ""), (("a",), "a"))
    _run("reverse_string_recursive", reverse_string_recursive,
         (("hello",), "olleh"), (("",), ""))
    _run("reverse_number", reverse_number,
         ((1234,), 4321), ((-120,), -21), ((0,), 0))
    _run("is_palindrome", is_palindrome, (("racecar",), True),
         (("hello",), False), (("",), True))

    print("\n--- B. Factorial & friends ---")
    _run("factorial_loop", factorial_loop, ((5,), 120), ((0,), 1), ((1,), 1))
    _run("factorial_recursive", factorial_recursive, ((5,), 120), ((0,), 1))
    _run("fibonacci", fibonacci,
         ((7,), [0, 1, 1, 2, 3, 5, 8]), ((1,), [0]), ((0,), []))
    _run("sum_of_digits", sum_of_digits, ((846210,), 21), ((0,), 0))
    _run("is_prime", is_prime, ((2,), True),
         ((17,), True), ((1,), False), ((25,), False))
    _run("gcd", gcd, ((25, 15), 5), ((7, 3), 1), ((15, 25), 5))

    print("\n--- C. Patterns (n = 4) ---")
    for fn in (right_triangle, inverted_triangle, pyramid, number_triangle, floyd_triangle, diamond):
        print(f"\n{fn.__name__}:")
        fn(4)
