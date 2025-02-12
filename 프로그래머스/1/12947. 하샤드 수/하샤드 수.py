def solution(x):
    x_list = list(map(int, str(x)))
    sum = 0 
    for i in range(len(x_list)):
        sum += x_list[i]
        
    if x % sum == 0:
        return True
    else :
        return False