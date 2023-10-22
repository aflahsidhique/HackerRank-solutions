# Time Conversion
#### In this problem, i write a function called timeConversion that takes a time string in 12-hour format as input and converts it to 24-hour format. The code then prompts the user to enter a time string and calls the timeConversion function to convert the input time.
```python
def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] != "12":
            s = str(int(s[:2]) + 12) + s[2:]
    else:
        if s[:2] == "12":
            s = "00" + s[2:]
    return s[:-2]
```

#### The timeConversion function takes a time string s as input. Here's how it works:
#### 1.The function checks if the last two characters of the input string s are "PM". If they are, it means the time is in the afternoon or evening.
#### 2.If the first two characters of the input string s are not "12", the function adds 12 to the hours portion of the time string to convert it to 24-hour format. It then concatenates the modified hours with the rest of the time string.
#### 3.If the last two characters of the input string s are not "PM", it means the time is in the morning.
#### 4.If the first two characters of the input string s are "12", the function replaces them with "00" to convert the time to 24-hour format.
#### 5.Finally, the function returns the converted time string without the last two characters (AM/PM).

```python
s = input()
result = timeConversion(s)
print(result)
```
#### First code prompts the user to enter a time string using the input() function and stores it in the variable s. 
#### It calls the timeConversion function with s as the argument and assigns the returned value to the variable result. 
#### Finally, it prints the converted time string using the print() function.

#### Sample input & output
##### input
```
07:05:45PM
```
##### output
```
19:05:45
```