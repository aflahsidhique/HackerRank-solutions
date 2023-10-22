## This python program is to print a StairCase Pattern
## Code ↓

```python
def print_stair(n):
   
    for i in range(1, n+1):
        for j in range(i, n):
            print(" ", end="")
        
        for k in range(1, i+1):
            print("#", end="")
        
        print()

if __name__ == "__main__":
    n= int(input("Enter the number of steps: "))
    print_stair(n)

```

## Expected Output
```
Enter the number of steps:5
    #
   ##
  ###
 ####
#####
```