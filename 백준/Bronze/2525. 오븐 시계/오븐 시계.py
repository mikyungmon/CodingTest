A, B = map(int, input().split())  # 현재 시각 A와 B
C = int(input())  # 요리하는 데 필요한 시간 C

new_A = (A+((B+C)//60))%24
new_B = (B+C)%60

print(new_A, new_B)