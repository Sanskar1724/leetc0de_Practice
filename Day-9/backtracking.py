"""Q. Given an integer array nums that may contain duplicates, return all possible subsets (the power set)."""


def subsetsWithDup(nums):
    res = []

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

# result= [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
