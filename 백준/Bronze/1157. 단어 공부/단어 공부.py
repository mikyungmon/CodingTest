word = input().upper()
word_dict = {}
max_cnt = 0
key_value = []

for i in word:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] +=1
 
for j in word_dict.values():
    max_cnt = max(max_cnt, j)
    
key_value = [k for k, v in word_dict.items() if v == max_cnt]

if len(key_value) == 1:
    print(key_value[0])
else:
    print('?')
    
    
    
    