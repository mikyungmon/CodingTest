def solution(s):
    p_counter = 0
    y_counter = 0
    for i in s:
        if i == 'p' or i == 'P':
            p_counter +=1
        elif i == 'y' or i == 'Y' :
            y_counter +=1
            
    if p_counter == y_counter :
        return True
    else :
        return False
        