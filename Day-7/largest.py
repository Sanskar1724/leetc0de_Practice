def largestNumber(self, nums: List[int]) -> str:
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            s = int(str(nums[j]) + str(nums[j+1]))
            t = int(str(nums[j+1]) + str(nums[j]))
            if t > s:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    if nums[0] == 0:
        return "0"
    return "".join([str(num) for num in nums])
