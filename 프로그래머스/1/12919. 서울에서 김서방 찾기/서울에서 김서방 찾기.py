def solution(seoul):
    for i in range(len(seoul)):
        if 'Kim' == seoul[i] :
            i = str(i)
            a = '김서방은'
            b = i + '에'
            c = '있다'
            return ('{} {} {}'.format(a,b,c))