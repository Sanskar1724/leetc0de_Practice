def findPeakElement(nums):
    arr = nums.copy()
    arr = sorted(arr)
    ele = arr[-1]
    return nums.index(ele)


print(f"Index of the peak element is {findPeakElement([14, 0, 4, 6, 42])}")
