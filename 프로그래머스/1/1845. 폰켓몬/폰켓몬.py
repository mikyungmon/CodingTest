def solution(nums):
    choose_num = len(nums)//2
    a = []
    for i in nums:
        if i not in a:
            a.append(i)
    exist_num = len(a)
    
    if(choose_num > exist_num):
        return exist_num
    elif (choose_num == exist_num) :
        return choose_num
    elif (choose_num < exist_num):
        return choose_num
