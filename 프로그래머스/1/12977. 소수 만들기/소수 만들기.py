from itertools import combinations

def solution(nums):
    choose_num = list(combinations(nums, 3))   # 조합
    result = 0
    for i in range(len(choose_num)):
        count = 0      # 약수의 개수
        for j in range(1,sum(choose_num[i])+1):
            if (sum(choose_num[i])) % j == 0:
                count +=1
        if count == 2:
            result +=1
            
    return result