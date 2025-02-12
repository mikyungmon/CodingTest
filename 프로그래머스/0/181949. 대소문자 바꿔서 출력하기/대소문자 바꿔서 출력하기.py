str = input()
str2 = []

for i in str:
    if i.islower():
        str2. append(i.upper())
    elif i.isupper():
        str2.append(i.lower())
        
print(''.join(str2))
    
