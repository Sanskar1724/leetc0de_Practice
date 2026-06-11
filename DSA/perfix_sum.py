# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
numbers = list(map(int, input("Enter input: ").split()))
sum_k = int(input("Enter k: "))
freq = {0: 1}


def prefix_sum(arr, k):
    n = len(arr)
    count = 0
    sumi = 0
    for i in range(n):
        sumi += arr[i]
        if sumi-k in freq:
            count += freq[sumi-k]
        freq[sumi] = freq.get(sumi, 0)+1
    return count


print(prefix_sum(numbers, sum_k))
