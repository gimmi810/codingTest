'''
Q. 숫자 카드 게임
    N * M 형태의 카드의 가장 높은 숫자가 쓰인 카드 한 장 뽑기

    조건 >>
    선택된 행의 카드들 중 가장 낮은 숫자의 카드를 뽑는다
    내가 뽑은 가장 낮은 숫자의 카드가 다른 행의 가장 낮은 수보다 커야한다.

    원리 >>
    그리디 알고리즘
    각 행마다 가장 작은 수를 찾은 뒤에 그 수중에서 가장 큰 수
'''

x, y = map(int, input('행, 열 숫자를 설정하세요: ').split())

smallest = []
for i in range(y):
    n = list(map(int, input().split()))
    smallest.insert(i+1, min(n))

print(max(smallest))



# 답안 예시 1 >>
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)




# 답안 예시 2 >>
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)