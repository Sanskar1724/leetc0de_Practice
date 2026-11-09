# Revision Day 1: Python basics, my mistakes

**Score:** 23 / 27 tests pass, 4 of 6 patterns correct.
Still to do: `is_prime` (empty), `right_triangle`, `inverted_triangle` (crashes), `number_triangle`, and the `floyd_triangle` start value.

## 1. Operator precedence (made this mistake 4 times)
`*` is applied before `+` and `-`.

| Wrote | Python reads it as | Fix |
|---|---|---|
| `fact * n-1` | `(fact*n) - 1` | `fact * (n-1)` |
| `" "*n-i-1` | `(" "*n) - i - 1` → TypeError | `" " * (n-i-1)` |
| `"*"*(2*i)+1` | `("*"*2i) + 1` → TypeError | `"*" * (2*i+1)` |
| `"*" * n-i` (inverted_triangle, still in file) | `("*"*n) - i` → TypeError | `"*" * (n-i)` |

**Rule:** when you multiply by an expression, wrap it in brackets: `x * (a - b)`.

## 2. Slicing
- `s[1:0]` is always `""` because the stop comes before the start. To get "everything from index 1", write `s[1:]`.

## 3. Loops
- **The pointer/variable never moved.** In palindrome I compared `s[0]` every time instead of `s[low]`, and never changed `high`. It passed "racecar" and "hello" by luck but failed on "abca". Always check that the pointers move.
- **Used `n` instead of the loop variable `i`** in factorial.
- **`range(n)` starts at 0.** For factorial or counting from 1, use `range(1, n+1)`.
- **Trace small inputs by hand** (write the variable after each pass). That catches all of the above.

## 4. Recursion
- **The base case must `return`.** Appending and then carrying on recurses forever.
- **The function must return a value.** Otherwise you get `None + None`, which is a TypeError.
- **Compute and collect separately:** recursion returns a value, and the caller builds the list.
- **Use base cases that cover edge cases:** `if s == ""` (not `len==1`), `if n <= 1`.
- **Don't use a modulo trick as a base case.** `len(s) % 10 == 0` is also true for length 10, 20, and so on.
- Naive recursive Fibonacci is O(2ⁿ). Use a loop with `a, b = b, a+b`.

## 5. Digit problems (`% 10`, `// 10`)
- `n % 10` gives the last digit, and `n // 10` removes it. Stop when `n == 0`.
- **Negative numbers:** `-1 // 10 == -1` in Python, so the loop never ends. Use `abs(n)` first.
- `rev = rev*10 + digit` builds the reversed number.

## 6. Patterns
- `print(x)` adds a newline. Use `print(x, end=" ")` inside the inner loop, then a plain `print()` after it.
- **Outer loop = row, inner loop = what goes in the row.**
- **Make a table with columns `i | spaces | stars`,** then find the formula for each column.
- **Read the expected output:** Floyd's triangle starts at 1, not 0. `right_triangle` needs `"* " * i`, not `"*"`.
- Diamond: the bottom half uses `range(n-2, -1, -1)` so the middle row isn't printed twice.

## 7. Small habits
- Don't name variables `sum`, `list` or `max`, because that hides the built-in.
- Use 4 spaces of indentation per level, consistently.
- `n // 2` is already an int, so `int()` isn't needed.

## Redo tomorrow without looking
`is_prime` (loop with `i*i <= n`), `inverted_triangle`, `number_triangle`, `floyd_triangle`.
