def solution(n):
    n = list(map(int,str(n)))  # map() : 첫번째 매개변수는 함수, 두번째는 반복 가능한 자료형 -> n = [1, 1, 8, 3, 7, 2]
    n.sort(reverse = True)
    result = ''.join(map(str, n)) 
    return int(result)