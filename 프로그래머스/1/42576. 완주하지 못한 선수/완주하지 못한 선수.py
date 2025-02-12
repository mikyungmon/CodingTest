def solution(participant, completion): 
    dict_par = {string : 0 for string in participant}
    # dict_par = dict.fromkeys(participant,0)

    for i in participant:
        dict_par[i] +=1
        
    for j in completion:
        dict_par[j] -=1
    
    for z in dict_par:
        if dict_par.get(z) ==1:
            return z
    
#     for i in dict_par.keys():
#         value = dict_par.get(i)
#         for j in range(len(participant)):
#             if participant[j] == i :
#                 value +=1
#                 dict_par[i] = value
        
#         for z in completion:
#             if i==z:
#                 value -=1
#                 dict_par[i] = value
        
#         if dict_par[i]!=0:
#             return i

#     for z in dict_par.keys():
#         if dict_par.get(z) !=0:
#             return z
        
    # print(dict_par)
    # print(dict_com)
    # 시간복잡도 때문에 list말고 딕셔너리로 풀어봐 딕셔너리(key:value)로
#     participant2 = participant.copy()   # participant2 = participant 이렇게하면 B수정시 A에도 반영 
#     for i in range(len(completion)):
#         count = 0
#         for j in range(len(participant)):
#             if participant[j] == completion[i]:
#                 count+=1
#                 if count == 1:
#                     participant2.remove(participant[j])  # 값지우기는 시간복잡도가 높아서 효율성 테스트 통과 못함
                
#     return participant2[0]          
        