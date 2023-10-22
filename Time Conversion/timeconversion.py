def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] != "12":
            s = str(int(s[:2]) + 12) + s[2:]
    else:
        if s[:2] == "12":
            s = "00" + s[2:]
    return s[:-2]

s = input()
result = timeConversion(s)
print(result)
