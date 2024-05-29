from collections import Counter, defaultdict
n = int(input())

dics = []

for _ in range(4):
    arr = list(map(int, input().split()))
    dics.append(Counter(arr))

A = defaultdict(int)
for item1 in dics[0].keys():
    for item2 in dics[1].keys():
        A[item1 + item2] = dics[0][item1] * dics[1][item2]

B = defaultdict(int)
for item1 in dics[2].keys():
    for item2 in dics[3].keys():
        B[item1 + item2] = dics[2][item1] * dics[3][item2]

answer = 0
for a in A.keys():
    if -a in B:
        answer += A[a] * B[-a]

print(answer)