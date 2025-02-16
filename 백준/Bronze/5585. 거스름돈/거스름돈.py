money = int(input())
coin = [500,100,50,10,5,1]
cnt = 0
exchange = 1000 - money
while exchange !=0 :
    for e in coin:
        if (exchange // e) >= 1:
            cnt += (exchange// e)
            exchange -= e * (exchange// e)
        else:
            continue    
print(cnt)
        