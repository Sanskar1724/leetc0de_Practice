def reverse(self, x: int) -> int:
    sign = -1 if x < 0 else 1

    x = abs(x)
    x = str(x)
    n = len(x)
    res = ""
    intlist = []
    # when you convert int into string you looss sign, so handle sign sepretly
    for ch in x:
        intlist.append(int(ch))
    low, high = 0, n-1

    while (low < high):
        intlist[low], intlist[high] = intlist[high], intlist[low]
        low += 1
        high -= 1
    while intlist:
        res += str(intlist.pop(0))
    ans = sign * int(res)
    # if num = 120 and you convert it into string and revere it, after that again convert it into int then 1st 0 gone
    if ans < -2**31 or ans > 2**31-1:
        return 0

    return ans
