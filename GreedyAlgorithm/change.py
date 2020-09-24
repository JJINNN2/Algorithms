n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # // 연산자는 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함. 일반적으로 C/C++에서 몫을 구할 때 사용하는 나누기 연산자랑 동일함.
    n %= coin

print(count)