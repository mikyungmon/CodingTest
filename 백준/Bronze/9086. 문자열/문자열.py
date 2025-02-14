n = int(input())
word = [input() for i in range(n)]

for i in word:
    print(i[0]+i[-1])