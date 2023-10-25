# Ice Cream Parlor

In this problem, we have a function called icecreamParlor that helps us find the indices of two ice cream flavors whose combined cost matches the given amount of money. The function takes two parameters: money (the amount of money we have) and cost (a list of costs for different ice cream flavors).
 
```python
def icecreamParlor(money, cost):
    cost_dict = {}
    
    for i, c in enumerate(cost, 1):
        if money - c in cost_dict:
            return [cost_dict[money - c], i]
        cost_dict[c] = i

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().split()))

        result = icecreamParlor(money, cost)

        print(*result)

```
1.The icecreamParlor function is defined, which takes money and cost as parameters.

2.Inside the function, a dictionary called cost_dict is initialized.

3.The cost list is iterated using the enumerate function.

4.For each iteration, the code checks if the complement cost (money - c) is present in the cost_dict.

5.If it is, the function returns a list containing the indices of the two flavors.

6.If not, the current cost (c) and its index (i) are added to the cost_dict.

7.The main code block checks for the number of test cases (t) and takes input for each test case.

8.The icecreamParlor function is called with the given budget (money) and the list of ice cream flavors' costs (cost).

9.The resulting indices are printed.
#### Sample input & output
input
```
STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
```

output
```
1 4
1 2
```
In this example, we have 5 ice cream flavors with costs [2, 5, 6, 7, 9]. We have 10 units of money. The function finds that the flavors at indices 1 and 4 (costs 5 and 9) have a combined cost of 10, so it returns [1, 4].