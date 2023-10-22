s, t = map(int, input().split())
a, b = map(int, input().split())
_, _ = map(int, input().split())  # Ignore m and n
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

count_Apples = sum(1 for apple in apples if s <= a + apple <= t)
count_Oranges = sum(1 for orange in oranges if s <= b + orange <= t)
print(count_Apples)
print(count_Oranges)