# Comparing Triplets in Python

#### In this code example, we have a function called ```compareTriplets``` that takes in two lists, a and b, representing the ratings of two people in three different categories. The function compares the ratings of each category and returns the number of points each person has earned.

```python
def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points

```
#### The ```compareTriplets``` function is defined, which takes in two lists, a and b.
#### Inside the function, a ```list called points``` is initialized with two elements, representing the ```points earned by Alice and Bob```.
#### A for loop is used to iterate over the ratings in the a and b lists.
#### Inside the loop, an if statement is used to compare the ratings of each category.
#### If ``` a is greater than b```, ```Alice earns a point```.
#### If  ```a is less than  b```, ```Bob earns a point```.
#### Finally, the ```points list is returned```.

```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = compareTriplets(a, b)
print(*result)
```
#### In this part, we take ```input from the user``` for the ratings of the two people. The ratings are entered as space-separated values. The map function is used to convert the input values to integers and store them in lists a and b. Then, we call the compareTriplets function with the a and b lists as arguments. The result is stored in the result variable. Finally, we use the print function with the * operator to unpack the elements of the result list and print them.
