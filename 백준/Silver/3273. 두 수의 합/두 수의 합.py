n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers_dict = {}
cnt = 0

for n in numbers:
    if n not in numbers_dict:
        numbers_dict[n] = 1

for a in numbers_dict.keys():
    if x - a in numbers_dict.keys():
        cnt +=1

print(cnt//2)
    
