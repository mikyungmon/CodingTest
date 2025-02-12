def solution(numbers):
    no = []    # 없는 수 
    for i in range(10):
        if i not in numbers :
            no.append(i)
            
    return(sum(no))