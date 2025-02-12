def solution(food):
    result = ""
    for i in range(1,len(food)):
        d = food[i] // 2
        result+= str(i) * d
        
    return result + "0" + ''.join(list(result)[::-1])  # 아래 코드를 한줄로!
        
#     result = result + "0"
    
#     result2 = list(result)
    
#     for j in range(len(result2)-2,-1,-1):
#         result2.append(result2[j])  
#     return ("").join(result2)