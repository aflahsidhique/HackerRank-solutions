def diagonalDifference(arr):
    n = len(arr)
    s1, s2 = 0, 0

    for i in range(n):
        s1 += arr[i][i]
        s2 += arr[i][n - i - 1]

    return abs(s1 - s2)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = diagonalDifference(arr)
print(result)
