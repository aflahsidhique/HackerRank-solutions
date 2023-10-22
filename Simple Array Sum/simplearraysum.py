# Function to calculate the sum of elements in an array
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Get user input for the array
try:
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    # Calculate the sum of the array
    result = calculate_sum(arr)

    # Print the sum
    print(f"The sum of the array is: {result}")

except ValueError:
    print("Please enter valid numbers for the array elements.")
