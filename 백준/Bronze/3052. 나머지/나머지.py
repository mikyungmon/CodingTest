numbers = [int(input()) for i in range(10)]
rest = []

for n in numbers:
    rest.append(n%42)

print(len(set(rest)))
