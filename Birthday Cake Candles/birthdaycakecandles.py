def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

# Input
candles_count = int(input())
candles = list(map(int, input().split()))

# Calculate and output the result
result = birthdayCakeCandles(candles)
print(result)
