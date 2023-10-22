def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = compareTriplets(a, b)
print(*result)
