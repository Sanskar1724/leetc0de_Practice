arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
max_water = 0
n = len(arr)
low = 0
high = n-1
while (low < high):
    area = min(arr[low], arr[high])*(high-low)
    max_water = max(max_water, area)
    if arr[low] < arr[high]:
        low += 1
    else:
        high -= 1


print(max_water)
