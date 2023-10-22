# Creating a Staircase Pattern in Python

#### To create the staircase pattern, we will use nested loops and the print() function in Python. The outer loop will iterate over the number of steps, and the inner loops will handle the printing of spaces and "#" symbols.


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
#### The ``` print_stair() ``` function takes an integer n as input, which represents the number of steps in the staircase. The function uses two nested loops to print the spaces and "#" symbols.

#### The outer loop iterates from 1 to n+1, representing the rows of the staircase. The inner loop, ``` for j in range(i, n)```, prints the spaces before the "#" symbols. The number of spaces decreases as we move down the rows.

#### The second inner loop, ```for k in range(1, i+1)```, prints the "#" symbols. The number of "#" symbols increases as we move down the rows.

#### Finally, the ```print()``` function is used to print a new line after each row of the staircase.

#### In the main block, the user is prompted to enter the number of steps. The input is converted to an integer using the int() function. Then, the print_stair() function is called with the user-provided input.

#### Sample input & output
##### input
```
Enter the number of steps: 5
```
##### output
```
    # 
   ##
  ###
 ####
#####
```

