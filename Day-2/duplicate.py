arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
n = len(arr)
# low = 0
# for high in range(1, n):
#     if arr[low] != arr[high]:
#         low += 1
#         arr[low] = arr[high]

# print(arr[0:low+1])
uniqe = []
for num in arr:
    if num in uniqe:
        continue
    uniqe.append(num)
print(uniqe)
