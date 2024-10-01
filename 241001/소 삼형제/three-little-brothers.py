'''
N번에 걸쳐 3 마리 소가 방을 드나든다.
지나갈때마다 농장 주인이 이름을 적는다. 
가장 많이 들어온 조합이 몇번 방에 들어왔는지 구한다. 

어떤 조합이 가장 많이 들어왔는지 보는 게임
'''
from collections import defaultdict
n = int(input())
# 순서가 상관없는 조합,, -> sorting후에 넣으면 되지 
arr = defaultdict(int)
for _ in range(n):
    names = tuple(sorted(input().split()))
    arr[names] += 1

items = sorted(arr.items(), key=lambda x: -x[1])
print(items[0][1])