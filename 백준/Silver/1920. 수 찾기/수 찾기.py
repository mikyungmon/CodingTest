n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_dict = {}

#{숫자:1} 형태 딕셔너리 생성
for i in a:
    if i not in a_dict:
        a_dict[i] = 1
        
for k in b:
    if k in a_dict.keys():
        print(1)
    else:
        print(0)