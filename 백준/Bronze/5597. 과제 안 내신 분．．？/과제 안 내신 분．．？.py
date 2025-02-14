student_nums = [int(input()) for i in range(28)]
not_submit = []

for a in range(1,31):
    if a not in student_nums:
        not_submit.append(a)

not_submit.sort()
print(not_submit[0])
print(not_submit[1])    
    