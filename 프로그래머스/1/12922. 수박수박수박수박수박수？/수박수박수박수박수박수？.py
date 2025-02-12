def solution(n):
    a = '수'
    b = '박'
    c = []
    result = []
    for i in range(5000):
        c.append(a)
        c.append(b)
        
    for j in range(n):
        result.append(c[j])
        
    result = ("".join(result))
    
    return result