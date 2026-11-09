arr = list(map(int, input("Enter sorted array seprerated by space:- ").split(" ")))
result = []
n = len(arr)
for i in range(n-2):
    # if necgative number is repeated
    if i > 0 and arr[i] == arr[i-1]:
        continue
    left, right = i+1, n-1
    z = -1 * arr[i]
    sumi = arr[left]+arr[right]
    while (left < right):
        if z == sumi:
            result.append([arr[i], arr[left], arr[right]])
            left += 1
            right -= 1
            while (left < n and arr[left] == arr[left-1]):
                left += 1
            while (right > 0 and arr[right] == arr[right+1]):
                right -= 1
        elif z < sumi:
            right -= 1
        else:
            left += 1

print(result)
