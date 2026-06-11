import heapq

# arr = list(
#     map(int, input("Enter sorted array seprerated by space:- ").split(" ")))

# this is used for top k element bottom ke element
array = [4, 8, 10, 3, 12]
# heapq.heapify(array)
# print(f"Result is min heap:-  {array}")

# max heap
# max_heap = []
# for num in array:
#     heapq.heappush(max_heap, -num)
# print(f"Result is negative integare max heap {max_heap}")

"""Q1. what is top 2 element in array"""

min_heap = []
array = [4, 8, 10, 3, 12]
result = []
for num in array:
    # print(len(min_heap))

    if len(min_heap) < 2:
        heapq.heappush(min_heap, num)

    else:
        element = min_heap[0]
        if element < num:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

# print(len(min_heap))

while min_heap:
    ele = heapq.heappop(min_heap)
    result.append(ele)
print(result[::-1])
