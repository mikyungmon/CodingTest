people_n = int(input())
per_people_time = list(map(int, input().split()))
pre_value = 0
time_list = []

per_people_time.sort()

for i in per_people_time:
    pre_value += i
    time_list.append(pre_value)
    
print(sum(time_list))
