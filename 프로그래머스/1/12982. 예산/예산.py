# from itertools import combinations

def solution(d, budget):
    d.sort()
    count = 0
    sum_num = 0
    for i in range(len(d)):
        sum_num += d[i]
        if sum_num <= budget:
            count+=1
    return count

# def solution(d, budget):
#     num = 0
#     for i in range(1,len(d)+1):
#         com=list(set(combinations(d, i)))
#         for j in range(len(com)):
#             if sum(com[j]) <= budget :
#                 num = len(com[j])
#     return num
        