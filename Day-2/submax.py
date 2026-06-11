s = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
freq = {}
n = len(s)
for right in range(n):
    freq[s[right]] = freq.get(s[right], 0)+1
    while len(freq) > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
            del freq[s[left]]
            left += 1
    if len(freq) == 1:
        res = max
