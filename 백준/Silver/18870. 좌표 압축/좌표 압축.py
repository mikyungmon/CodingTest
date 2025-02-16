n = int(input())
numbers = list(map(int, input().split()))
numbers_dict = {}
result = [0] * n
        
for n in range(len(numbers)):
    if numbers[n] not in numbers_dict:
        numbers_dict[numbers[n]] = [n]
    else:
        numbers_dict[numbers[n]].append(n)

numbers_dict_sort = sorted(numbers_dict.items(), key=lambda x:x[0])

for index,(number,idx) in enumerate(numbers_dict_sort):
    for i in idx:
        result[i] = index
        
print(*result)  # 결과 리스트를 출력
