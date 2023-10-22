# Counting Birthday Cake Candles
For this problem, we write a function called birthdayCakeCandles that takes in a list of candle heights as input and returns the count of the tallest candles. The code also includes an input section where the user can provide the number of candles and their heights.

```python
def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count
```
 The birthdayCakeCandles function takes in a list of candle heights as input.
 It finds the maximum height using the max() function.
 It counts the number of candles with the maximum height using the count() method.
 It returns the count of the tallest candles.
```python
# Input
candles_count = int(input())
candles = list(map(int, input().split()))

```
The input section prompts the user to enter the number of candles and their heights.
The input is processed and stored in the candles_count and candles variables.
The birthdayCakeCandles function is called with the candles list as an argument.
```python
# Calculate and output the result
result = birthdayCakeCandles(candles)
print(result)

```
 The result is stored in the result variable.
 The result is printed to the console.

#### Sample input & output
input
```
4
3 2 1 3
```
output
```
2
```
In this example, we have a list of candle heights [3,2,1,3]. The tallest candles have a height of 3, and there are 2 candles with that height. Therefore, the output is 2.