'''
moo를 계속 출력하는 게임
S(0)은 "m o o"로 시작하고, 그 다음부터
S(1) = S(1-1) + m ooo = o *(t + 2) + S(0)
    = m o o m ooo m oo
dp 네

하나씩 미리 저장한 후에 점차 참고해서 큰 값을 알아내는 것
그 전 것들만 알고 있으면 되네?
근데 S(1) = 
N 까지의 길이에 무엇이 나올지 예측하면 됨
계산해서


규칙을 찾자
S(1) = “ m o o m o o o m o o “ = 10
S(2) = “ m o o m o o o m o o m o o o o m o o m o o o m o o ” = 25 = 20 + 2 + 3
S(3) = " m o o m o o o m o o m o o o o m o o m o o o m o o
         m o o o o o 
         m o o m o o o m o o m o o o o m o o m o o o m o o
         = 50 + t + 3 만큼 = 56
10 25 56 56 * 2 + 
이 안에 들어간다 싶으면 

2 3 2 
moo 
'''
# length = [0] * 40
# length[0] = 3
# def find_step(num):
#     for step in range(1, 28):
#         length[step] = length[step - 1] * 2 + step + 3
#         if length[step - 1] < num and num <= length[step]:
#             return step

# def dfs(step):
#     if step == 0:
#         return "moo"
#     return dfs(step - 1) + "m" + "o" * (step + 2) + dfs(step - 1)

# length = [0] * 40
# length[0] = 3
# step = 0
# N = int(input())
# index = N - 1
# if N > 3:
#     step = find_step(N)
#     print(length[step], step)
#     if N > length[step] // 2:
#         N = length[step] - N
#         step = find_step(N)
#         index = N + 1
#         print()

# word = "moo"
# for i in range(1, step + 1):
#     word = word + "m" + "o" * (i + 2) + word

# print(word[index])


def find_nth_moo(N):
    # 각 단계에서 S(t)의 길이를 재귀적으로 계산하는 함수
    def get_length(t):
        if t == 0:
            return 3  # S(0)은 "moo"로 길이가 3
        return 2 * get_length(t - 1) + (t + 3)
    
    # 재귀적으로 N번째 문자를 찾는 함수
    def solve(t, N):
        if t == 0:
            # S(0)은 "moo"이므로 간단하게 처리 가능
            return "moo"[N - 1]
        
        len_prev = get_length(t - 1)  # S(t-1)의 길이
        
        if N <= len_prev:
            # N이 첫 번째 S(t-1)에 속하는 경우
            return solve(t - 1, N)
        elif N > len_prev + (t + 3):
            # N이 두 번째 S(t-1)에 속하는 경우
            return solve(t - 1, N - len_prev - (t + 3))
        else:
            # N이 중간의 "moo...o"에 속하는 경우
            if N == len_prev + 1:
                return 'm'
            else:
                return 'o'
    
    # 단계 t를 찾아서 해결
    t = 0
    while get_length(t) < N:
        t += 1
    
    return solve(t, N)

# 입력 및 실행
N = int(input())
print(find_nth_moo(N))