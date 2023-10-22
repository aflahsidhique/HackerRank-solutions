# Grading Students
In this problem, I created a program that takes input for the number of grades to be entered, and then prompts the user to enter each grade. The program then rounds each grade according to a specific rule and prints the rounded grades.
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
