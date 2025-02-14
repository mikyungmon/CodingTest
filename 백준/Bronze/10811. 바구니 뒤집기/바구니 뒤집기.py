n,m = map(int, input().split())
ij_list = [tuple(map(int, input().split())) for i in range(m)]
numbers = []

for a in range(1,n+1):
    numbers.append(a)
    
for t in ij_list:
    numbers[t[0]-1:t[1]] = reversed(numbers[t[0]-1:t[1]])
    
print(' '.join(map(str, numbers)))