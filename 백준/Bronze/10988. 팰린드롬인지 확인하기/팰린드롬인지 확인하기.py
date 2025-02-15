word = input()
word_list = []

for i in word:
    word_list.append(i)
    
reverse_word = list(reversed(word_list))

if word_list == reverse_word:
    print(1)
else:
    print(0)