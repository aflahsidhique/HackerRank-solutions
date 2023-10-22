# Apples and Oranges
In this code, we are given the coordinates of a house and the positions of apple and orange trees. We need to count the number of apples and oranges that fall within a certain range of the house.

```python
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split()) 
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

count_Apples = sum(1 for apple in apples if s <= a + apple <= t)
count_Oranges = sum(1 for orange in oranges if s <= b + orange <= t)
print(count_Apples)
print(count_Oranges)
```

#### countApplesAndOranges has the following parameter(s):
s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.

##### The code uses list comprehension and the sum() function to count the number of apples and oranges that fall within the given range. It iterates over the apples and oranges lists, checking if the sum of the tree position and the distance of the fruit from the tree falls within the range s to t. If it does, it increments the count by 1.
##### The code prints the number of apples and oranges that land on Sam's house.

#### Sample input & output
input
```
7 11
5 15
3 2
-2 2 1
5 -6
```
output
```
1
1
```
the range is from 7 to 11. The apple tree is at position 5, and the orange tree is at position 15. The apples fall at distances -2, 2, and 1 from the tree, while the oranges fall at distances 5 and -6 from the tree. Only one apple and one orange fall within the range, so the output is 1 for both.