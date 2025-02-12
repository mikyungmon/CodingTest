def solution(price, money, count):
    use_money = 0
    for i in range(1,count+1):
        use_money += price * i
        
    if use_money >= money :
        answer = use_money - money
        return answer
    else:
        return 0
    