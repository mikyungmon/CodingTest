def solution(k, m, score):
    sort_score = sorted(score,reverse=True)  # 내림차순 정렬
    
    box = []
    price = 0
    for i in range(0,len(sort_score)-m+1,m):
        box.append(sort_score[i:i+m])
    
    for i in box:
        price += min(i) * len(i)
        
    return price