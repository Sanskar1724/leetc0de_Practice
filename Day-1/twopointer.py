# Two sum problem
arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
target = int(input("Enter Target:- "))
length = len(arr)
low = 0
high = length-1

while (low < high):
    sumi = arr[low]+arr[high]
    if sumi == target:
        print(
            f"Target is {sumi} gott it and numbers are {arr[low]} and {arr[high]}")
        break
    elif sumi < target:
        low = low+1
    else:
        high = high-1
