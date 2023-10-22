# Plus Minus
The plusMinus function is a Python function that takes an array of integers as input and calculates the ratio of positive, negative, and zero elements in the array. It then prints these ratios with a precision of 6 decimal places.

```python
def plusMinus(arr):
    n = len(arr)
    countPositive = sum(1 for num in arr if num > 0)
    countNegative = sum(1 for num in arr if num < 0)
    countZero = n - countPositive - countNegative

    print(f"{countPositive/n:.6f}")
    print(f"{countNegative/n:.6f}")
    print(f"{countZero/n:.6f}")
```
 ```sum(1 for num in arr if num > 0)```: This expression uses a generator expression to count the number of positive elements in the array. It iterates over each element num in the array arr and increments the count by 1 if the element is greater than 0.

 ```sum(1 for num in arr if num < 0)```: This expression counts the number of negative elements in the array using a similar approach as above, but checks if the element is less than 0.

 ```n - countPositive - countNegative```: This expression calculates the number of zero elements in the array by subtracting the counts of positive and negative elements from the total number of elements in the array.


 The function takes an array arr as input and performs the calculations to determine the ratios of positive, negative, and zero elements. It then prints these ratios.

```python
#Input
n = int(input())
arr = list(map(int, input().split()))

plusMinus(arr)
```
 In this part, the user is prompted to enter the number of elements in the array (n). Then, the user is asked to enter the elements of the array separated by spaces. 
 
 The map function is used to convert the input string into a list of integers. Finally, the plusMinus function is called with the array as the argument.

#### Sample input & output
input
```
3
5 -3 2
```
output
```
0.666667
0.333333
0.000000
```