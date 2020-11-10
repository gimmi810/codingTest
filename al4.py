'''
Q. 1이 될 때까지
    N이 1이 될때까지 수행하는 최소 횟수 구하기

    조건 >>
    N에서 1을 뺀다
    N을 K로 나눈다
    N은 K보다 항상 크거나 같다

    원리 >>
    최대한 많이 나누기
'''

n, k = map(int, input('N, K를 입력하시오: ').split())

cnt = 0

while n != 1:
    if (n % k) == 0:
        n = n / k
    else:
        n -= 1

    cnt += 1

print(cnt)




# 답안 예시1 >>
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)



# 답안 예시2 >>
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)
