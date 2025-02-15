n = int(input())
words = [input() for _ in range(n)]

words_set = list(set(words))    # 중복 단어 제거
words_dict = {}
reverse_dict = {}    # 키와 밸류를 뒤집기
result_dict = {}

for w in words_set:
    if w not in words_dict:
        words_dict[w] = len(w)

# 길이(value값)를 기준으로 정렬
sort_words_len = sorted(words_dict.items(), key=lambda x: x[1])  # sorted(정렬할 대상, 정렬기준)

# 딕셔너리 키 밸류 뒤집기(길이가 작은 값부터 정렬된 상태)
for k,v in sort_words_len:   # sort_words_len.items() 하면 안 됨 -> sorted 결과는 튜플의 리스트로 저장되기 때문
    if v not in reverse_dict :
        reverse_dict[v] = [k]
    else:
        reverse_dict[v].append(k)
        
# 길이가 같은 게 있다면 사전 순으로
for v in reverse_dict :
    reverse_dict[v] = sorted(reverse_dict[v])

# 다시 딕셔너리 키 밸류 뒤집기
for key, value in reverse_dict.items():
    for v in value:
        result_dict[v] = key

for kk in result_dict.keys():
    print(kk)