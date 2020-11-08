'''
Q. 큰 수의 법칙
    주어진 자연수들의 조건에 맞는 가장 큰 합계 구하기

    조건 >>
    N : 배열의 크기
    M : 숫자가 더해지는 횟수
    K : 연속 가능 횟수

    원리 >>
    그리디 알고리즘
'''

n, m, k = map(int, input('N, M, K 숫자를 설정하세요: ').split())
num_list = list(map(int, input('자연수를 입력하세요: ').split()))

sort_num = sorted(num_list, reverse=True)
sum_num = 0
j = 0

for i in range(0, m):
    if j < k:
        sum_num += sort_num[0]
        j += 1
        print(sort_num[0])
    else:
        sum_num += sort_num[1]
        j = 0
        print(sort_num[1])

print(sum_num)


# 답안 예시 >>
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)