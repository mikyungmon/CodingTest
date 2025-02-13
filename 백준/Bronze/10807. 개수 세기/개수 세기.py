N = int(input())  # 정수 개수 입력
numbers = list(map(int, input().split()))  # N개의 정수 입력
v = int(input())  # 찾을 정수 v 입력

# v의 개수 세기
print(numbers.count(v))  
