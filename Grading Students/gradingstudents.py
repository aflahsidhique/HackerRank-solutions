n = int(input().strip())

for _ in range(n):
    grade = int(input().strip())
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)

    print(grade)
