n = int(input())
len_way = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
total_len = sum(len_way)
expense = 0
min_price = oil_price[0]

for o in range(1,len(oil_price)):   
    if min_price > oil_price[o]:
        expense += min_price * len_way[o-1]
        min_price = oil_price[o]
       
    elif min_price <= oil_price[o]:
        expense += min_price * len_way[o-1]
        
print(expense)       
