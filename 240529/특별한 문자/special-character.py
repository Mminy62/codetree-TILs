from collections import defaultdict
dic = defaultdict(int)
word = list(input())
for i, v in enumerate(word):
    dic[v] += 1

# 가장 먼저 등장한걸 출력..
# 개수를 key, 값을 value, index
result = []
for k, v in dic.items():
    if v == 1:
        result.append(k)

if len(result) == 1:
    print(result[0])
else:
    ans = len(word)
    for c in result:
        ans = min(ans, word.index(c))
    
    print(word[ans])