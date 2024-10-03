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


'''

length = [0] * 40
length[0] = 3
step = 0
N = int(input())

if N > 3:
    for i in range(1, 24):
        length[i] = length[i - 1] * 2 + i + 3
        if length[i - 1] < N and N <= length[i]:
            step = i
            break

# step 까지만 string을 만든다.
word = "moo"
if step > 1:
    for i in range(1, step + 1):
        word = word + "m" + "o" * (i + 2) + word

print(word[N - 1])