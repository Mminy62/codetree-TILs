from itertools import permutations

# 소 이름
cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]

# N 줄
N = int(input())

# 
constraints = []
for _ in range(N):

    parts = input().split()
    A = parts[0]
    B = parts[-1]

    constraints.append((A, B))

def valid_order(perm):
    index_map = {cow: idx for idx, cow in enumerate(perm)}
    # 옆에 있는지 확인하기 위해서 abs로 index 차이값을 확인한다.
    for a, b in constraints:
        if abs(index_map[a] - index_map[b]) != 1:
            return False

    return True

sorted_cows = sorted(cows)

for perm in permutations(sorted_cows):
    if valid_order(perm):

        for cow in perm:
            print(cow)
        break