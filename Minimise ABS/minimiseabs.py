def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1))

n = int(input())
arr = list(map(int, input().split()))
result = minimumAbsoluteDifference(arr)
print(result)
