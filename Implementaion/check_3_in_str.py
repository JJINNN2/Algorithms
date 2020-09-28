n = int(input())

result = 0

for i in range(n+1):    # n+1이 아니라 n만 하면 n까지가 아니라 n미만까지 반복.
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)