# Minimum Absolute Difference in an Array
In this problem, we are given a list of numbers and our task is to find the minimum absolute difference between any two numbers in the list. The absolute difference between two numbers is the positive difference between them, regardless of their order.

```python
    def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1))
```


The minimumAbsoluteDifference function takes a list arr as input. 

It first sorts the list using the sort() method, which arranges the elements in ascending order. 

Then, it uses a generator expression to calculate the absolute difference between each pair of adjacent elements in the sorted list. 

Finally, it returns the minimum absolute difference using the min() function.


```python
n = int(input())
arr = list(map(int, input().split()))
result = minimumAbsoluteDifference(arr)
print(result)
```
In the main program logic, we first read an integer n from the user, which represents the number of elements in the list. 

Then, we read the elements of the list from the user as space-separated integers and convert them into a list using the map() and list() functions. 

Next, we call the minimumAbsoluteDifference function with the list as an argument and store the result in the variable result. 

Finally, we print the minimum absolute difference.

#### Sample input & output
input
```
5
1 5 3 9 2
```
output
```
1
```
The code will calculate the minimum absolute difference among the numbers [1, 5, 3, 9, 2]. 

After sorting the list, we get [1, 2, 3, 5, 9]. 

The absolute differences between adjacent numbers are [1, 1, 2, 4]. 

The minimum absolute difference is 1, so the code will output 1.