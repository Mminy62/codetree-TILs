from collections import defaultdict

n, k = map(int, input().split())

arr = list(map(int, input().split()))
dic = defaultdict(int)
for key in arr:
    dic[key] += 1

answer = 0

for num in set(arr):
    cnt = dic[num]
    remain = k - num
    if remain == num:
        answer += cnt * (cnt - 1) // 2
    else:
        answer += cnt * (dic[remain])
    
print(answer)