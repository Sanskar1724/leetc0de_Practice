# using kadanes find max sum of substring
a = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
# bestend = a[0]
# ans = a[0]
# for i in range(1, len(a)):
#     v1 = bestend+a[i]
#     v2 = a[i]
#     bestend = max(v1, v2)
# ans = max(bestend, ans)

# print(ans)

# findig subarray with max product
# maxend = a[0]
# ans = a[0]
# minend = a[0]
# for i in range(1, len(a)):
#     v1 = maxend*a[i]
#     v2 = minend*a[i]
#     v3 = a[i]
#     maxend = max(max(v1, v2), v3)
#     minend = min(min(v1, v2), v3)
# ans = max(maxend, minend)
# print(ans)

# Circlur array max sum
# here we need to use
# minsum = a[0]
# maxsum = a[0]
# g_max = a[0]
# g_min = a[0]
# total_sum = a[0]
# ans = a[0]
# for i in range(1, len(a)):
#     v1 = maxsum+a[i]
#     v2 = a[i]
#     maxsum = max(v1, v2)
#     g_max = max(maxsum, g_max)

#     v3 = minsum + a[i]
#     v4 = a[i]
#     minsum = min(v3, v4)
#     g_min = min(g_min, minsum)
#     total_sum += a[i]
#     diff = total_sum - g_min

# if g_max < 0:
#     print(g_max)
# else:
#     print(max(total_sum-g_min, g_max))

# maximum sum in one deleation possible
nodelete = a[0]
onedelete = 0
ans = a[0]
for i in range(1, len(a)):
    prevno = nodelete
    prevone = onedelete

    nodelete = max(prevno+a[i], a[i])
    onedelete = max(prevone+a[i], prevno)
    ans = max(nodelete, onedelete, ans)
print(ans)
