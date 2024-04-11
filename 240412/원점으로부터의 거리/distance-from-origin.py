'''
번호가 작은 점부터 출력
원점에서 가까운 점부터 순서대로 번호를 출력
점의 위치 주어짐
원점은 0, 0
거리가 같으면 번호가 작은 것부터 출력
1~ N개 
'''
import heapq

N = int(input())
info = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    heapq.heappush(info, (abs(x) + abs(y), i))

for _ in range(N):
    print(heapq.heappop(info)[-1])