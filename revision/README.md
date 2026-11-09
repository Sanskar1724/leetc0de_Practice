# Revision

Second pass over everything in `Day-1` … `Day-9`: re-solving each problem, fixing old bugs, and writing down mistakes.

## How each topic folder works

```
NN-topic-name/
├── practice.py       ← problems to solve (stubs + tests). Run it, aim for all PASS
├── mistakes.md       ← what I got wrong; re-read before the next attempt
└── optimization.md   ← complexity, better versions, interview follow-ups
```

Run any practice file from the repo root:
```bash
python revision/01-python-basics/practice.py
```

**Revision loop:** read `mistakes.md` → solve `practice.py` without looking → run the tests → add new mistakes to `mistakes.md`.

## Progress

| # | Topic | Folder | Original code | Status |
|---|---|---|---|---|
| 01 | Python basics: reverse, factorial, primes, GCD, patterns | [01-python-basics](01-python-basics/) | Day-6, Day-8 | 🟡 24/28 tests pass. To fix: `is_prime`, 4 patterns |
| 02 | Two pointers: Two Sum, Container With Most Water, 0s/1s, 3Sum | [02-two-pointers](02-two-pointers/) | Day-1, Day-3 | ⬜ Next. Fix the 3Sum bug (`sumi` is never recomputed) |
| 03 | Sliding window | – | Day-2/submax.py | ⬜ `submax.py` is unfinished |
| 04 | Kadane / 1-D DP | – | Day-3/kadane.py | ⬜ Max product: update `ans` inside the loop |
| 05 | Prefix sum + hashmap | – | Day-4, DSA/perfix_sum.py | ⬜ |
| 06 | Stack | – | Day-4/stack.py | ⬜ |
| 07 | Binary search (incl. search on answer) | – | Day-5/binary.py, Day-7/peak.py | ⬜ Aggressive cows `low` bound, peak in O(log n) |
| 08 | Heap / top-k | – | Day-5/heap.py | ⬜ |
| 09 | Linked list: fast & slow | – | Day-3, DSA/fast_and_slow.py | ⬜ |
| 10 | Sorting tricks / math | – | Day-6, Day-7 | ⬜ |
| 11 | Recursion & backtracking | – | Day-8, Day-9 | ⬜ Subsets II: `res = ()` crash, no duplicate skip |

⬜ not started · 🟡 in progress · ✅ all tests pass, mistakes reviewed

## Not covered yet (after revision)
Trees · Tries · Graphs (BFS/DFS) · 2-D DP
