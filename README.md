# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.


## 1.Apple and Orange

  - [Problem](https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Apple_and_Orange/appleandorange.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we are given the coordinates of a house and the positions of apple and orange trees. We need to count the number of apples and oranges that fall within a certain range of the house.

  ```python
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split()) 
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

count_Apples = sum(1 for apple in apples if s <= a + apple <= t)
count_Oranges = sum(1 for orange in oranges if s <= b + orange <= t)
print(count_Apples)
print(count_Oranges)
```

#### countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.

t: integer, ending location of Sam's house location.

a: integer, location of the Apple tree.

b: integer, location of the Orange tree.

apples: integer array, distances at which each apple falls from the tree.

oranges: integer array, distances at which each orange falls from the tree.

 The code uses list comprehension and the sum() function to count the number of apples and oranges that fall within the given range. It iterates over the apples and oranges lists, checking if the sum of the tree position and the distance of the fruit from the tree falls within the range s to t. If it does, it increments the count by 1.
 The code prints the number of apples and oranges that land on Sam's house.
#### Sample input & output
input
```
7 11
5 15
3 2
-2 2 1
5 -6
```
output
```
1
1
```
the range is from 7 to 11. The apple tree is at position 5, and the orange tree is at position 15.

The apples fall at distances -2, 2, and 1 from the tree, while the oranges fall at distances 5 and -6 from the tree. 

Only one apple and one orange fall within the range, so the output is 1 for both.

****

## 2.Birthday Cake Candles

  - [Problem](https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Birthday_Cake_Candles/birthdaycakecandles.py) (navigate to the Solution file)
  - Explanation:
  > For this problem, we write a function called birthdayCakeCandles that takes in a list of candle heights as input and returns the count of the tallest candles. The code also includes an input section where the user can provide the number of candles and their heights.

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

****

## 3.Compare The Tripplets
  - [Problem](https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Compare_The_Tripplets/comparethetriplets.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we have a function called ```compareTriplets``` that takes in two lists, a and b, representing the ratings of two people in three different categories. The function compares the ratings of each category and returns the number of points each person has earned.

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
 The ```compareTriplets``` function is defined, which takes in two lists, a and b.

 Inside the function, a ```list called points``` is initialized with two elements, representing the ```points earned by Alice and Bob```.

 A for loop is used to iterate over the ratings in the a and b lists.

Inside the loop, an if statement is used to compare the ratings of each category.

If ``` a is greater than b```, ```Alice earns a point```.

If  ```a is less than  b```, ```Bob earns a point```.

Finally, the ```points list is returned```.

```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = compareTriplets(a, b)
print(*result)
```
 In this part, we take ```input from the user``` for the ratings of the two people. The ratings are entered as space-separated values. The map function is used to convert the input values to integers and store them in lists a and b. Then, we call the compareTriplets function with the a and b lists as arguments. The result is stored in the result variable. Finally, we use the print function with the * operator to unpack the elements of the result list and print them.


#### Sample input & output
input
```
4 5 6
7 5 3
```
output
```
1 1
```
****
## 4.Diagonal Difference

  - [Problem](https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Diagonal_Difference/diagonaldifference.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we have to calculate the diagonal difference in a square matrix. The diagonal difference is the absolute difference between the sums of its diagonals.

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
****
## 4.Grading Students
  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Grading_Students/gradingstudents.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, I created a program that takes input for the number of grades to be entered, and then prompts the user to enter each grade. The program then rounds each grade according to a specific rule and prints the rounded grades.
```python
n = int(input().strip())

for _ in range(n):
    grade = int(input().strip())
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)

    print(grade)

```

It takes input for the number of grades to be entered as n.

 It uses a for loop to iterate over the range of the number of grades.

 Inside the loop, it takes input for each grade.

 It checks if the grade is greater than or equal to 38 and if the remainder of the grade divided by 5 is greater than or equal to 3.

 If the condition is true, it rounds the grade by adding the difference between 5 and the remainder of the grade divided by 5.
 
 Finally, it prints the rounded grade.

```
n = int(input().strip())  # Enter the number of grades: 3

for _ in range(n):
    grade = int(input().strip())  # Enter the grades: 73, 67, 41
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)
    
    print(grade)
Output:

75
67
41
```
In this example, we entered 3 grades: 73, 67, and 41. The first grade, 73, is rounded up to 75 because the remainder of 73 divided by 5 is 3, which is greater than or equal to 3. The second grade, 67, remains the same because the remainder of 67 divided by 5 is 2, which is less than 3. The third grade, 41, also remains the same because it is less than 38.
****
## 5.Mini-Max Sum

  - [Problem](https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Mini-Max_Sum/minimaxsum.py) (navigate to the Solution file)
  - Explanation:
  >This problem  takes an array of integers as input and calculates the minimum and maximum sums of four out of the five elements in the array.

#### The miniMaxSum function takes an array (arr) as input and performs the following steps:

 1.Sorts the array in ascending order using the sort() method.

 2.Calculates the sum of all elements except the last one using the sum() function and slicing (arr[:-1]).

 3.Calculates the sum of all elements except the first one using the sum() function and slicing (arr[1:]).

 4.Prints the minimum sum and maximum sum.

 code with an example. Consider the following input:

```python
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)

```
 The miniMaxSum function will perform the following steps:

 Example input: arr = 5 2 3 4 1

 ```arr.sort()```: Sorts arr in ascending order = [1,2,3,4,5]

 ```sum(arr[:-1])```: Calculate the minimum sum by removing last element of array: 1+2+3+4 = 10

 ```sum(arr[1:])```: Calculate the maximum sum by removing first element of array: 2+3+4+5= 14

 Print the minimum sum: 10
 
 Print the maximum sum: 14

#### Sample input & output
input
```
1 3 5 7 2 6
```
output
```
17 23
```
****
## 6.Plus Minus

  - [Problem](https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true) (navigate to the Problem)
  - [Solution](Plus_Minus/plusminus.py) (navigate to the Solution file)
  - Explanation:
  >The plusMinus function is a Python function that takes an array of integers as input and calculates the ratio of positive, negative, and zero elements in the array. It then prints these ratios with a precision of 6 decimal places.

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
****
## 7.Simple Array Sum

  - [Problem](https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true) (navigate to the Problem)
  - [Solution](Simple_Array_Sum/simplearraysum.py) (navigate to the Solution file)
  - Explanation:
  >In this problem, we will be calculating the sum of elements in an array using Python. The code prompts the user to enter the number of elements in the array and then takes input for each element. It then calculates the sum of the array and prints the result.

```python
# Function to calculate the sum of elements in an array
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
```
 The calculate_sum function takes an array (arr) as input and initializes a variable total to 0. It then iterates over each element in the array and adds it to the total variable. Finally, it returns the total sum.

```python
# Get user input for the array
try:
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
```
 In this part of the code, we prompt the user to enter the number of elements in the array (n). We then initialize an empty list arr to store the elements. Using a for loop, we iterate n times and ask the user to enter each element. The element is then appended to the arr list.

```python
    # Calculate the sum of the array
    result = calculate_sum(arr)

    # Print the sum
    print(f"The sum of the array is: {result}")

except ValueError:
    print("Please enter valid numbers for the array elements.")
```
 After obtaining the user input, we call the calculate_sum function with the arr list as the argument. The returned sum is stored in the result variable. Finally, we print the sum of the array using an f-string.

 In case the user enters invalid numbers for the array elements (non-integer values), a ValueError exception is raised, and an error message is displayed.

#### Sample input & output
input
```
Enter the number of elements in the array: 5
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Enter element 5: 5
```
output
```
The sum of the array is: 15
```
****
## 8.StairCase

  - [Problem](https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true) (navigate to the Problem)
  - [Solution](Staircase/Staircase.py) (navigate to the Solution file)
  - Explanation:
  >To create the staircase pattern, we will use nested loops and the print() function in Python. The outer loop will iterate over the number of steps, and the inner loops will handle the printing of spaces and "#" symbols.


```python
def print_stair(n):
    for i in range(1, n+1):
        for j in range(i, n):
            print(" ", end="")
        
        for k in range(1, i+1):
            print("#", end="")
        
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of steps: "))
    print_stair(n)
```
The ``` print_stair() ``` function takes an integer n as input, which represents the number of steps in the staircase. The function uses two nested loops to print the spaces and "#" symbols.

The outer loop iterates from 1 to n+1, representing the rows of the staircase. The inner loop, ``` for j in range(i, n)```, prints the spaces before the "#" symbols. The number of spaces decreases as we move down the rows.

The second inner loop, ```for k in range(1, i+1)```, prints the "#" symbols. The number of "#" symbols increases as we move down the rows.

Finally, the ```print()``` function is used to print a new line after each row of the staircase.

In the main block, the user is prompted to enter the number of steps. The input is converted to an integer using the int() function. Then, the print_stair() function is called with the user-provided input.

#### Sample input & output
input
```
Enter the number of steps: 5
```
output
```
    # 
   ##
  ###
 ####
#####
```
