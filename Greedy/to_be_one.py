# map(자료형, 값)과 split(구분되는 기 문자, 미입력시 공백)을 이용하여 공백을 기준으로 입력받기
n, k = map(int, input().split())

quotient = n  # input값인 n을 훼손하지 않기 위함
result = 0

while True:
    if quotient == 1:
        break
    quotient //= k
    result += 1

remainder = n - ((n // k) * k)
result += remainder

print(result)

#31:36
