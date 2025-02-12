def solution(s):
    s_sort = sorted(s)  # str type은 sort메소드 없다. sorted(s)처럼 가능. 대신 return type은 list
    answer = []
    for i in range(len(s_sort)-1,-1,-1):
        answer.append(s_sort[i])
        
    return ("".join(answer))  # list -> str