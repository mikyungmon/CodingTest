def solution(s, n):
    alp_to_int = []
    int_to_alp = []
    for i in s:
        alp_to_int.append(ord(i) - 64)  # 공백 -> 숫자: -32, ord(문자) : 문자에 해당하는 유니코드 반환
    print(alp_to_int)
    
    for z in range(len(alp_to_int)):
        # 대문자 Z->A에 대해서 
        if (alp_to_int[z] != -32) and (alp_to_int[z ]< 33) :
            alp_to_int[z]=alp_to_int[z]+n

            if (27 <= alp_to_int[z]):
                alp_to_int[z] = alp_to_int[z]-26
                
        # 소문자 z->a에 대해서 
        elif (alp_to_int[z] != -32) and alp_to_int[z] >=33 :
            alp_to_int[z]=alp_to_int[z]+n
            if (59 <= alp_to_int[z]):
                alp_to_int[z] = alp_to_int[z]-26
    
    for w in alp_to_int :
        int_to_alp.append(chr(int(w)+64)) # chr(정수) : 정수에 해당하는 유니코드 문자 반환
    
    return("".join(int_to_alp))
    