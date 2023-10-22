# Diagonal Difference
In this problem, we have to calculate the diagonal difference in a square matrix. The diagonal difference is the absolute difference between the sums of its diagonals.

The diagonalDifference function takes a square matrix as input and calculates the diagonal difference.

```python
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
```
 
It uses two variables, s1 and s2, to store the sums of the elements on the primary and secondary diagonals, respectively. 

It iterates over the rows of the matrix and adds the corresponding element to the sums. Finally, it returns the absolute difference between s1 and s2.

The main program prompts the user to enter the size of the matrix (n) and then takes n lines of input, each containing n space-separated integers. It creates a 2D list arr to store the matrix. 

It then calls the diagonalDifference function with arr as the argument and assigns the result to the variable result. 

Finally, it prints the result.

#### Sample input & output
input
```
3
1 2 3
4 5 6
7 8 9
```
 the size of the matrix = 3

The primary diagonal elements are 1, 5, and 9, and their sum is 1 + 5 + 9 = 15. 

The secondary diagonal elements are 3, 5, and 7, and their sum is 3 + 5 + 7 = 15.

The absolute difference between the sums of the primary and secondary diagonals is |15 - 15| = 0.

output
```
0
```
