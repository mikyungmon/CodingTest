n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()

for a in numbers:
    print(a)
    