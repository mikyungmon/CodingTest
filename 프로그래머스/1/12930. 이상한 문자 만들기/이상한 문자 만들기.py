def solution(s):
    s = s.split(' ')  # 공백 기준으로 나눈다
    result = []
    for i in range(len(s)):
        str_list = list(s[i])
        for j in range(len(s[i])):
            if j%2 == 0 :
                str_list[j] = str_list[j].upper()   
            else :
                str_list[j] = str_list[j].lower()
                
        string = ''.join(str_list)
        result.append(string)  # 단어 하나하나 list마다 변환된 값 출력
    answer = ' '.join(result)
    return answer