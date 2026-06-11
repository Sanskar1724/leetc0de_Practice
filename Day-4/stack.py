# stack is to get most recent element
# it is use like in real life problems likes matching cancelling cleaning
# s = "saannskar"
ans = ""
stack = []
# for i in range(len(s)):
#     if stack and stack[-1] == s[i]:
#         stack.pop()
#     else:
#         stack.append(s[i])
# while stack:
#     ans += stack.pop()
#     # print(ans)
# print(ans[::-1])

# valid paranthesis

para = "({}[]())"
valid = True
for ch in para:
    if ch == "[" or ch == "(" or ch == "{":
        stack.append(ch)
    else:
        if not stack:
            valid = False
        elif ch == "]" and stack[-1] == "[":
            stack.pop()
        elif ch == ")" and stack[-1] == "(":
            stack.pop()
        elif ch == "}" and stack[-1] == "{":
            stack.pop()
        else:
            valid = False
if stack:
    valid = False

if valid:
    print("VAlid para")
else:
    print("Not a valid")
