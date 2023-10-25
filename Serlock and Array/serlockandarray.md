# Serlock and Array
In this code, we are given an array of integers and we need to determine if there exists an element in the array such that the sum of all the elements to its left is equal to the sum of all the elements to its right. If such an element exists, we return "YES", otherwise we return "NO".

To solve this problem, we need to iterate through the array and calculate the total sum of all the elements. Then, we iterate through the array again and keep track of the left sum. At each iteration, we check if the left sum multiplied by 2 is equal to the total sum minus the current element. If it is, then we have found a balanced sum and we return "YES". If we finish iterating through the array without finding a balanced sum, we return "NO".


1.The balancedSums function takes an array arr as input and returns "YES" or "NO" based on whether a balanced sum exists or not.

2.Inside the balancedSums function, we calculate the total sum of the array using the sum function and store it in the variable total.

3.We initialize the variable left_sum to 0, which will keep track of the sum of elements to the left of the current element.

4.We iterate through the array using a for loop and perform the following steps:
> Check if the left sum multiplied by 2 is equal to the total sum minus the current element. If it is, we have found a balanced sum and we return "YES".
> Add the current element to the left sum.

5.If we finish iterating through the array without finding a balanced sum, we return "NO".

6.In the main section of the code, we take the number of test cases as input and iterate through them.

7.For each test case, we take the number of elements in the array as input and then take the array elements as input.

8.We call the balancedSums function with the array as input and store the result in the variable result.

9.Finally, we print the result.

Code Examples
Here is an example of how to use the balancedSums function:

```python
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

```
#### Sample input & output
input
```
2
3
1 2 3
4
1 2 3 3 
```

output
```
NO
YES
```
For the first test case, no such index exists.

For the second test case,arr[0]+arr[1]=arr[3] , therefore index  satisfies the given conditions.
