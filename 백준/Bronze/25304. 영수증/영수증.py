total = int(input())
n = int(input())
items = [tuple(map(int, input().split())) for i in range(n)]
expend = 0

for t in range(len(items)):
    expend +=items[t][0] * items[t][1]
    
if total == expend:
    print('Yes')
else:
    print('No')

