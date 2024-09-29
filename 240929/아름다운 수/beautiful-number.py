'''
숫자만큼, 연달아서 수가 나오면 아름다운 수


2자리 -> 
10 ** (n - 1) ~ 10 ** n - 1

문자열로 반환 -> count가 0이면 max_count = 설정
count == max_count => count = 0, max_count = 0
처음에 0이면 설정하고 조건 확인하기

'''

# n자리 아름다운 수의 개수를ㅊㄹ력한다. 

n = int(input())
result = 0

def is_beautiful(nums):
    count = 0
    max_count = 0
    pre = ""
    for num in nums:
        if count == 0:
            max_count = int(num)
            pre = num
            count = 1
        else:
            if pre == num:
                count += 1
        
        if count > max_count:
            return False
        
'''
한 글자가 나왔을때 앞에거하고 다르면 그때 연속 카운트를 비교해야지
한 글자에서 쭉 이어나가는게 백트래킹
'''

for number in range(10 ** (n - 1), 10 ** n):
    arr = list(str(number))