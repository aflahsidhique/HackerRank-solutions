#This program prints a pattern of '#' in a StairCase method.
def print_stair(n):
   #Prints a Stair Case pattern of '#' with n steps.
    #n: Number of Steps in a stair case.
  
    for i in range(1, n+1):
        # Print spaces before the '#' in each step
        for j in range(i, n):
            print(" ", end="")
        
        # Print '#' in each step
        for k in range(1, i+1):
            print("#", end="")
        
        # jump to the next line
        print()

if __name__ == "__main__":
    n= int(input("Enter the number of steps: "))
    print_stair(n)
