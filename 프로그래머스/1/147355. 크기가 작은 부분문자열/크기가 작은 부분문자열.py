def solution(t, p):
    numbers = []
    result = 0
    for i in range(len(t)-len(p)+1):
        numbers.append(t[i:i+len(p)])
    
    for j in numbers :
        if int(j) <= int(p):
            result +=1
    
    return result