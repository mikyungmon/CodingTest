def solution(strings, n):
    
    ch = []
    strings2 = []
    cut = []
    
    for i in range(len(strings)):
        ch.append(strings[i][n])
        strings2.append(ch[i] + strings[i])
        strings2.sort()
        print(strings2)
        
    for j in range(len(strings2)):
            cut.append(strings2[j][1:])
        
    return cut