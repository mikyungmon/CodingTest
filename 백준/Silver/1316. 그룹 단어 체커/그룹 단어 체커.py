n = int(input())
word = [input() for i in range(n)]
result = 0

for w in word:
    word_dict = {}
    val_list = []

    for a in range(len(w)):
        if w[a] not in word_dict:
            word_dict[w[a]] = [a]
        else:
            word_dict[w[a]].append(a)

    for k,v in word_dict.items():
        val_list.append(v)
        
    # 같은 문자 그룹 내 연속성 체크
    cnt = 1
    for seq in range(len(val_list)):
        # 현재 그룹이 연속적인지 확인
        if not all(val_list[seq][i] + 1 == val_list[seq][i + 1] for i in range(len(val_list[seq]) - 1)):
            cnt = 0  # 하나라도 연속하지 않으면
            break
            
    # 문자 그룹끼리 연속성 체크
    if cnt == 1:  # 첫 번째 체크가 통과하면, 그룹 간 연속성 체크 시작
        for seq2 in range(len(val_list)-1):
            if val_list[seq2][-1] + 1 != val_list[seq2 + 1][0]:
                cnt = 0  # 그룹 간 연속이 아니면 cnt를 0으로 리셋
                break  # 더 이상 체크할 필요 없으므로 종료
            
    if cnt == 1:
        result +=1
print(result)
