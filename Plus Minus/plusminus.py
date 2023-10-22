def plusMinus(arr):
    n = len(arr)
    countPositive = sum(1 for num in arr if num > 0)
    countNegative = sum(1 for num in arr if num < 0)
    countZero = n - countPositive - countNegative

    print(f"{countPositive/n:.6f}")
    print(f"{countNegative/n:.6f}")
    print(f"{countZero/n:.6f}")

# Input
n = int(input())
arr = list(map(int, input().split()))

plusMinus(arr)
