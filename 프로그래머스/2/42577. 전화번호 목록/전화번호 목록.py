# 첫 시도 -> 정확도 66.7/100.0 -> 
# def solution(phone_book):
#     phone_book_dict = {}
    
#     for i in range(len(phone_book)):
#         if phone_book[i] not in phone_book_dict:
#             phone_book_dict[phone_book[i]] = i
#         else:
#             continue

#     sub_list = []
#     for key in phone_book_dict:
#         sub = [k for k in phone_book_dict.keys() if key in k]   # 문제지점 : 접두사가 아닌 포함여부만 체크
#         sub_list.append(sub)
    

#     if any(len(i)>1 for i in sub_list):
#         return False
#     else:
#         return True
    
    
# 두 번째 시도
# def solution(phone_book):
#     phone_book.sort()
#     phone_book_dict = {}
    
#     for i in range(len(phone_book)):
#         if phone_book[i] not in phone_book_dict:
#             phone_book_dict[phone_book[i]] = i
#         else:
#             continue
    
#     for key in phone_book_dict:
#         for k in phone_book_dict.keys():  # 문제지점 : 이중 for문으로 복잡도 이슈
#             if k != key :
#                 if(k.startswith(key)):
#                     return False

#     return True
                
# 세 번째 시도 
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
            if phone_book[i+1].startswith(phone_book[i]):
                return False
    
    return True
    
    
        
        