# Задание №1

N = int(input())
num = list(map(int, input().split()))
count = len(set(num))
print(count)


# Задание №2

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

count = len(set(l1) & set(l2))
print(count)

# Задание №3

num = list(map(int, input().split()))
sequence = set()

for x in num:
    if x in sequence:
        print("YES")
    else:
        print("NO")
        sequence.add(x)