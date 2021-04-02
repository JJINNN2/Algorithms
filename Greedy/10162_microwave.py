t = int(input())

arr = [300, 60, 10]
count = [0, 0, 0]

if t % 10 != 0:
    print(-1)
else:
    for idx in range(len(arr)):
        count[idx] += t // arr[idx]
        t %= arr[idx]

    print(count[0], count[1], count[2])
