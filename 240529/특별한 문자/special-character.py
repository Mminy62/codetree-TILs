from collections import defaultdict

dic = defaultdict(int)
word = list(input())

for v in word:
    dic[v] += 1

ans = "None"
for c in word:
    if dic[c] == 1:
        ans = c
        break

print(ans)