arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
n = len(arr)
low = 0
high = n-1
while (low < high):
    while (low < n and arr[low] == 0):
        low += 1
    while (high > 0 and arr[high] == 1):
        high -= 1
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1

print(arr)
