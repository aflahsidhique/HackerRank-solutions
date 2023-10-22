# Mini-Max Sum
#### This problem  takes an array of integers as input and calculates the minimum and maximum sums of four out of the five elements in the array.

### The miniMaxSum function takes an array (arr) as input and performs the following steps:

#### Sorts the array in ascending order using the sort() method.
#### Calculates the sum of all elements except the last one using the sum() function and slicing (arr[:-1]).
#### Calculates the sum of all elements except the first one using the sum() function and slicing (arr[1:]).
#### Prints the minimum sum and maximum sum.

#### code with an example. Consider the following input:

```python
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)

```
#### The miniMaxSum function will perform the following steps:
#### Example input: arr = 5 2 3 4 1
#### ```arr.sort()```: Sorts arr in ascending order = [1,2,3,4,5]
#### ```sum(arr[:-1])```: Calculate the minimum sum by removing last element of array: 1+2+3+4 = 10
#### ```sum(arr[1:])```: Calculate the maximum sum by removing first element of array: 2+3+4+5= 14
#### Print the minimum sum: 10
#### Print the maximum sum: 14
 ###Expected Output
 ```
 5 2 3 4 1
 10 14
 ```