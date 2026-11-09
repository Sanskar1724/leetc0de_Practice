# Revision Day 1: optimization and revision notes

For each problem: **the approach to remember**, its time and space complexity, the optimized or Pythonic version, and what an interviewer might ask next.

---

## A. Reverse

### Reverse a string
| Approach | Time | Space | Note |
|---|---|---|---|
| `rev = ch + rev` in a loop (yours) | **O(n²)** | O(n) | Strings are immutable, so every `+` copies the whole string |
| Recursion `rev(s[1:]) + s[0]` (yours) | **O(n²)** | O(n) stack | `s[1:]` copies the string on every call; crashes for n > ~1000 |
| List + two pointers, then `"".join` | O(n) | O(n) | The interview answer |
| `s[::-1]` | O(n) | O(n) | The Pythonic one-liner |

```python
def reverse_string(s):
    chars = list(s)
    low, high = 0, len(chars) - 1
    while low < high:
        chars[low], chars[high] = chars[high], chars[low]
        low += 1
        high -= 1
    return "".join(chars)
```
**Rule:** build a list and call `"".join()` once at the end. Never use `+=` on a string inside a loop.

**O(n) recursion** (pass indexes instead of slices):
```python
def rev(chars, low, high):
    if low >= high:
        return
    chars[low], chars[high] = chars[high], chars[low]
    rev(chars, low + 1, high - 1)
```
Related LeetCode problems: 344 Reverse String (in-place) and 541 Reverse String II.

### Reverse a number
Yours is already optimal: **O(d) time, where d = number of digits (that's log₁₀ n), and O(1) space.**
Follow-up (LeetCode 7): if the result goes outside the 32-bit range `[-2³¹, 2³¹-1]`, return 0. Check this before the multiply step:
```python
if rev > (2**31 - 1) // 10: return 0
```
Your Day-6 version used `str()` and `pop(0)`. `pop(0)` is O(n) per call, so that whole version is O(n²). Avoid `list.pop(0)`; use `collections.deque.popleft()` instead.

### Palindrome
Two pointers: **O(n) time, O(1) space.** `s == s[::-1]` is also O(n) but uses O(n) extra space.
Follow-ups:
- **LeetCode 125:** ignore non-alphanumeric characters. Skip them with `while low < high and not s[low].isalnum(): low += 1`, and compare with `.lower()`.
- **LeetCode 680:** you may delete one character. On the first mismatch, check `s[low+1:high+1]` or `s[low:high]`.
- **LeetCode 9, palindrome number without str():** reverse only half the digits, stopping when `rev >= n`.

---

## B. Factorial and similar

### Factorial
| Approach | Time | Space |
|---|---|---|
| Loop | O(n) | **O(1)** |
| Recursion | O(n) | **O(n) call stack** |

Prefer the loop. Python's default recursion limit is about 1000 (`sys.getrecursionlimit()`). Python **does not** optimise tail calls, so even "tail-recursive" code still uses stack space.
Built-in: `math.factorial(n)`.
Follow-up (LeetCode 172): count the trailing zeros of n! without computing it. Count the factors of 5: `n//5 + n//25 + n//125 + ...`

### Fibonacci
| Approach | Time | Space |
|---|---|---|
| Naive recursion `f(n-1)+f(n-2)` | **O(2ⁿ)** | O(n) |
| Recursion + memo (`@lru_cache`) | O(n) | O(n) |
| Loop `a, b = b, a+b` (yours) | O(n) | O(1) to get the nth number, O(n) to build the list |

```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
```
**This is your first DP idea:** naive recursion recomputes the same subproblems, and memoization stores them. Climbing Stairs (LeetCode 70) is the same problem as Fibonacci.

### Sum of digits
O(d) time, O(1) space, which is optimal. Fixes: use `abs(n)` first (otherwise negatives loop forever) and don't name a variable `sum`.
One-liner: `sum(int(c) for c in str(abs(n)))`
Follow-up (LeetCode 258, Add Digits until a single digit remains): the O(1) formula is `0 if n == 0 else 1 + (n - 1) % 9`.

### Prime check
| Approach | Time |
|---|---|
| Try every divisor 2…n-1 | O(n) |
| Try up to √n (`i*i <= n`) | **O(√n)** |
| Handle 2 separately, then only test odd numbers | O(√n / 2) |

```python
def is_prime(n):
    if n < 2: return False
    if n < 4: return True          # 2, 3
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
```
**Many primes up to N, use the Sieve of Eratosthenes (LeetCode 204):** O(N log log N).
```python
def count_primes(n):
    if n < 3: return 0
    is_p = [True] * n
    is_p[0] = is_p[1] = False
    i = 2
    while i * i < n:
        if is_p[i]:
            for j in range(i * i, n, i):   # start at i*i: smaller multiples are already crossed out
                is_p[j] = False
        i += 1
    return sum(is_p)
```

### GCD
Euclid: **O(log min(a, b))**. Order doesn't matter: `gcd(15, 25)` swaps itself on the first step (15 % 25 = 15).
- Built-in: `math.gcd(a, b)`
- LCM: `a * b // gcd(a, b)`, or `math.lcm` in Python 3.9+
- Recursive one-liner: `def gcd(a, b): return a if b == 0 else gcd(b, a % b)`

---

## C. Patterns

All patterns are **O(n²)** because they print about n² characters. You can't do better, since that much output has to be printed.

**The method, every time:**
1. Make a table with columns `row i | spaces | symbols | what's printed`
2. Find each column's formula in terms of `i` and `n`
3. Outer loop = rows, inner loop (or string multiplication) = what's on the row

**Cheat sheet (rows i = 0..n-1):**
| Pattern | Spaces | Symbols |
|---|---|---|
| Right triangle | 0 | `i+1` |
| Inverted triangle | 0 | `n-i` |
| Right-aligned triangle | `n-i-1` | `i+1` |
| Pyramid | `n-i-1` | `2i+1` |
| Inverted pyramid | `i` | `2(n-i)-1` |
| Diamond | pyramid, then `range(n-2, -1, -1)` | same formulas |

**Faster printing:** calling `print()` thousands of times is slow. Build the rows and print once:
```python
rows = [" " * (n-i-1) + "*" * (2*i+1) for i in range(n)]
print("\n".join(rows))
```
Using `" ".join(map(str, range(1, i+1)))` for number rows also gets rid of the trailing space.

Try these next: hollow square, hollow pyramid, Pascal's triangle (LeetCode 118, which is also a DP warm-up), and a 0-1 alternating triangle.

---

## Big-O summary to memorise
| Problem | Best time | Space |
|---|---|---|
| Reverse string | O(n) | O(n), or O(1) in place on a list |
| Reverse number / sum of digits | O(log n) | O(1) |
| Palindrome | O(n) | O(1) |
| Factorial | O(n) | O(1) |
| Fibonacci (nth) | O(n) | O(1) |
| Prime check | O(√n) | O(1) |
| All primes < N | O(N log log N) | O(N) |
| GCD | O(log min(a, b)) | O(1) |
| Patterns | O(n²) | O(1), or O(n²) if you build the output first |

## Python performance habits
- Use `"".join(list)`, not `+=` on strings in a loop.
- Avoid `list.pop(0)` and `x in list` inside loops. Both are O(n). Use `deque` and `set`.
- Write `i * i <= n` instead of `i <= n ** 0.5` to avoid float rounding.
- Prefer loops over deep recursion, since Python has no tail-call optimisation and a limit of about 1000 calls.
- Know the built-ins: `math.factorial`, `math.gcd`, `math.isqrt`, `functools.lru_cache`.
