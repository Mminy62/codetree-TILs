n, m = map(int, input().split())
# 최대 가치 순으로 담는다. m까지 
bags = []
for _ in range(n):
    w, v = map(int, input().split())
    bags.append([(v/w), w])

bags.sort(key = lambda x: (-x[0], -x[1]))
ans = 0
# 키로당 가치 
for item in bags:
    value, weight = item
    if weight < m:
        m -= weight
        ans += weight * value

    else: # weight >= m
        ans += value * m
        break

print(format(round(ans, 3), '.3f'))