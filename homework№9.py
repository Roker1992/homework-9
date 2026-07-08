# Задание №1

N = int(input())
numbers = list(map(int, input().split()))
count = len(set(numbers))
print(count)