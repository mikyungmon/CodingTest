def solution(name, yearning, photo):
    result = []
    idx = []

    for i in range(len(photo)):
        idx.clear() 
        plus_year = 0
        
        for j in photo[i]:
            for k in range(len(name)):
                if name[k] == j :
                    idx.append(k) 
        for z in idx:
            plus_year += yearning[z]
        
        result.append(plus_year)
        
    return result