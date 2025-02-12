def solution(s):
    s_dict = dict.fromkeys(s,0)
    print(s_dict)
    
    s_list = list(s)
    # print(s_list)
        
    for i in s_dict.keys() :
        s_dict[i] = list(filter(lambda x: s[x] == i, range(len(s))))
    
    # print(s_dict)
    
    for j in s_dict.keys():
        if len(s_dict.get(j)) == 1:
            s_list[s_dict.get(j)[0]] = -1
        elif len(s_dict.get(j)) > 1:
            s_list[s_dict.get(j)[0]] = -1
            for z in range(1,len(s_dict.get(j))):
                # print('111111111111111',s_dict.get(j)[z])
                # print('222222222222222', s_dict.get(j)[z-1] )
                s_list[s_dict.get(j)[z]] = s_dict.get(j)[z] - s_dict.get(j)[z-1] 
    
    return s_list
                
                
                
                
                
#         print('zzzzz', s_list)
#             # s_list[z] = -1 
            
#     print(s_list)
#         s_list[s_dict.get(j)[0]] = -1
    
#         for z in range(len(s_dict.get(j))):
#             print('z',z)
        
#     answer = []
#     idx=[]
#     a =[]
    
#     for i in s :
#         idx.append(list(filter(lambda x: s[x] == i, range(len(s)))))
#     print(idx)
    
#     s_list = list(s)
#     print('s_list',s_list)
    
#     for j in range(len(idx)):
#         if (len(idx[j])) == 1:
#             s_list[j] = int(-1)
#         elif type(s_list[j]) != 'int':
#             s_list[idx[j][0]] = int(-1)
            
#     print(s_list)
                
                
# #     for i in list(s):
# #         idx.append(s.index(i))
# #     print(idx)
    
# #     for j in idx:
# #         if idx.count(j) == 1:
# #             answer.append(int(-1))
# #         else:
# #             a.append(list(filter(lambda x: idx[x] == j, range(len(idx)))))
# #     print('a',a)
# #     print('answer',answer)
# #     # for i in range(len(s)):
    
# # #     for i in s:
# # #         cnt.append(s.count(str(i)))
# # #         print('cnt', cnt)
    
# # #     for j in range(len(cnt)):
# # #         if cnt[j] == 1:
# # #             answer.append(int(-1))
# # #         elif 
# #     # return answer