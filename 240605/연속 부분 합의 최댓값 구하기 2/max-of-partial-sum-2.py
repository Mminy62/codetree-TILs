'''
시간을 줄이기위한 그리디 -> 완탐으로 풀지 X

'''
import sys
n = int(input())
arr = list(map(int, input().split()))
ans = 0
result = -sys.maxsize
for item in arr:
    if ans >= 0:
        ans += item
    else: # 음수인 경우 
        ans = item
    
    result = max(result, ans)
        
print(result)