def solution(sizes):
    garo = []
    sero = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1] : 
            garo.append(sizes[i][0])
            sero.append(sizes[i][1])
        else:
            sero.append(sizes[i][0])
            garo.append(sizes[i][1])
        
    return max(garo) * max(sero)
    
