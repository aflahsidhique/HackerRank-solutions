# Calculating the Sum of Elements in an Array
 In this problem, we will be calculating the sum of elements in an array using Python. The code prompts the user to enter the number of elements in the array and then takes input for each element. It then calculates the sum of the array and prints the result.

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