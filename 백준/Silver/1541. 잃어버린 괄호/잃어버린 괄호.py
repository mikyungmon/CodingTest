expression = input().strip()
result = 0

# - 기준으로 자름
exp_part = expression.split('-')

# - 나오기 전 그룹은 다 더해줌
result = sum(map(int, exp_part[0].split('+')))

# - 이후에 나온 그룹은 다 빼줌
for e in exp_part[1:]:
    result -= sum(map(int, e.split('+')))

print(result)