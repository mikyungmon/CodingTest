def solution(n):
    n2 = n-1
    list_ = []
    for i in range(1,n):
        if n2 % i == 0 :
            list_.append(i)

    return list_[1]