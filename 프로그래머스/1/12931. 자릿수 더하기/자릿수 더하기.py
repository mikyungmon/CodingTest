def solution(n):
    list_ = []
    result = 0
    for i in str(n):
        list_.append(int(i))
        
    for j in range(len(list_)):
        result +=list_[j]
        
    return result