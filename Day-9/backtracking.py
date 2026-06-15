"""Q. Given an integer array nums that may contain duplicates, return all possible subsets (the power set)."""


def subsetsWithDup(nums):
    res = ()

    def fun(arr, n, idx, temp):
        if idx == n:
            # if temp in res:
            #     continue
            res.append(temp[:])
            return
        fun(arr, n, idx+1, temp)

        temp.append(arr[idx])
        fun(arr, n, idx+1, temp)
        temp.pop()
    fun(nums, len(nums), 0, [])
    return res


array = [1, 2, 3]
print(subsetsWithDup(array))

result = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
"""Q Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 """
nums = [1, 2, 3]


def subsets(nums):
    nums.sort()
    res = []

    def fun(start, temp):
        if temp not in res:
            res.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            fun(i+1, temp)
            temp.pop()
    fun(0, [])
    return res


print(subsets(nums))
# result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
