def balancedSums(arr):
    total = sum(arr)
    left_sum = 0
    
    for num in arr:
        if left_sum * 2 == total - num:
            return "YES"
        left_sum += num
    
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())

    for _ in range(T):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        result = balancedSums(arr)
        print(result)
