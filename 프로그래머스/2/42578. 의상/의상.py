# 첫 번째 시도
# def solution(clothes):
#     clothes_dict = {}
#     result_sum = 0
#     result_multiply = 1

#     for i in range(len(clothes)):
#         if clothes[i][1] not in clothes_dict.keys():
#             clothes_dict[clothes[i][1]] = []
#         clothes_dict[clothes[i][1]].append(clothes[i][0])
    
#     if len(clothes_dict.keys()) == 1:
#         return len(sum(list(clothes_dict.values()),[]))
#     else: 
#         for j in clothes_dict.keys():
#             result_sum += len(clothes_dict.get(j))
#             result_multiply *= len(clothes_dict.get(j))
            
#         return result_sum + result_multiply
    
# 두 번째 시도
def solution(clothes):
    clothes_dict = {}
    combination_check = 1

    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_dict.keys():
            clothes_dict[clothes[i][1]] = []
        clothes_dict[clothes[i][1]].append(clothes[i][0])

    if len(clothes_dict.keys()) == 1:
        return len(sum(list(clothes_dict.values()),[]))
    else: 
        for j in clothes_dict.keys():
            combination_check *= (len(clothes_dict.get(j)) + 1)
        
        combination_check -=1
        
        return combination_check