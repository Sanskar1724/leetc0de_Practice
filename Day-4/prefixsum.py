arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
k = int(input("Enter number:-"))
freq = {0: 1}
sumi = 0
count = 0
# for i in range(len(arr)):
#     sumi += arr[i]
#     if sumi-num in freq:
#         count += freq[sumi-num]
#     freq[sumi] = 1

# print(count)
""" here crack is we are saving every prefsum in hash, now if any prefsum-k is appred in hashmap mean
sumi = prefsum-k, till in loop prefixsum = sumi is appeeed remaing is k
quation says k = prefsum-sumi , so prefum-sum is remaining part and that is substring """

# Now qeation of finding sum whose reminder is equal to k
for i in range(len(arr)):
    sumi += arr[i]
    rem = sumi % k
    if rem < 0:
        rem = rem+k
    if rem in freq:
        count += freq[rem]
    freq[rem] = freq.get(rem, 0)+1
print(count)
