# now we start binary, it is vast topic and many type of question can be framed in it.
# most basic question in binary to seach a number in array using logn
arr = list(
    map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
# its need sortedf array
# target = int(input("Enter number to find:- "))
# n = len(arr)
# # arr = sorted(arr)
# low, high = 0, n
# while (low <= high):
#     geuss = (low+high)//2
#     if arr[geuss] == target:
#         print(f"Found target at {geuss+1} index")
#         # you have to right break because of low<=high low can be equal to high
#         break
#     elif arr[geuss] < target:
#         low = geuss+1
#     else:
#         high = geuss-1

"""Question 1 :- find ceil in int array"""
# array = [1 5 9 16 20 25 36 25 17 12 9 3]
# n = len(array)
# res = 0
# low, high = 0, n-1
# while (low < high):
#     geuss = (low+high)//2
#     if array[geuss] < array[geuss+1]:
#         low = geuss+1
#     else:
#         res = geuss
#         high = geuss-1

# print(res)

""" Q2. find minimum element in sorted array"""
# # arr = [12 13 15 17 27 0 1 2 3]
# res = -1
# n = len(arr)
# low, high = 0, n-1
# while (low <= high):
#     geuss = (low+high)//2
#     if arr[geuss] > arr[n-1]:
#         low = geuss+1
#     else:
#         res = arr[geuss]
#         high = geuss-1

# # print(res)

""" Q.3 koko eating banana problem"""
# h = int(input("Enter number of hours returning guard:- "))
# n = max(arr)
# m = 1


# def hours(array, k):
#     hours = 0
#     n = len(array)
#     for i in range(n):
#         # your are fuvkinh ideot, only  one mistake that cause 30 min is fucking division ans modullo because ure fallow prebious wrong this which is in you mind

#         hours += array[i] // k
#         if array[i] % k != 0:
#             hours += 1

#     return hours


# low, high = m, n
# res = 0
# while (low <= high):
#     geuss = (low+high)//2
#     if hours(arr, geuss) > h:
#         low = geuss+1
#     else:
#         res = geuss
#         high = geuss-1
# print(res)

""" Q4.  aggresive cows"""
k = int(input("Enetr number of cows you have to add:- "))
res = 0


def speed(array, geuss, k):
    n = len(array)
    array = sorted(array)
    cows = 1
    prevcow = array[0]
    for i in range(1, n):
        dis = array[i]-prevcow
        if dis < geuss:
            continue
        else:
            cows += 1
            prevcow = array[i]
    if cows >= k:
        return True
    else:
        return False


low, high = min(arr), max(arr)
while (low <= high):
    geuss = (low+high)//2
    if speed(arr, geuss, k):
        res = geuss
        low = geuss+1
    else:
        high = geuss-1
print(res)
