def solution(left, right):
    num = []
    counts = []  # 약수 개수 리스트
    sum_num = 0
    for i in range(left, right+1):
        num.append(i)
    
    for j in num:
        count = 0 
        for k in range(1,j+1):
            if j % k == 0:
                count +=1
        counts.append(count)

    for a in range(len(counts)):
        if counts[a] % 2 ==0:
            sum_num += num[a]
        else:
            sum_num -= num[a]
            
    return sum_num
            
            
    