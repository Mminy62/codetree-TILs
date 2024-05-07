'''
문자열 A, (, ) 
() 쌍의 수 세기 
(를 스택으로 쌓아놓고 )나오면 그 갯수를 반환
'''

arr = list(input())
stack = []
ans = 0
for c in arr:
    if c == "(":
        stack.append(c)
    else:
        ans += len(stack)

print(ans)