def solution(n):
    numbers=[True] * (n+1)  # 0~n 리스트 생성
    numbers[0], numbers[1] = False, False  # 0,1은 소수가 아니니까 제외
    end = int(n**(1/2)) # n의 제곱근
    
    for i in range(2, end+1):  # 2 ~ n제곱근까지 
        for j in range(i*i, n+1, i):  # 4부터 i만큼씩 증가시키면서 배수면 false로 바꿈
            if numbers[j]:
                numbers[j] = False
                
    return numbers.count(True)
#     numbers=[]
#     for a in range(2,n+1):
#         numbers.append(a)
        
#     end = int(n**(1/2)) # n의 제곱근
#     rem = []
#     for i in range(2, end+1):
#         for j in range(i+1, n+1):
#             if j % i == 0 :
#                 rem.append(j)
                
#     answer = list(set(numbers) - set(rem)) 
    
#     return len(answer)

#     for j in numbers:
#         for z in range(j+1,n+1):
#             if z % j == 0 :
#                 delete.append(z)
    
#     answer = list(set(numbers) - set(delete))    
    
#     return len(answer)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def solution(n):
#     numbers = [] # 1과 숫자 n사이의 수가 담긴 리스트
#     divisor = [] # n의 약수가 담긴 리스트
#     count = 0
#     for i in range(1,n+1):
#         numbers.append(i) 
#         for j in range(1,i+1):
#             if i%j == 0 :
#                 divisor.append(j)
#         if len(divisor) == 2:
#             count+=1
#             divisor.clear()  
#         else:
#             divisor.clear()
            
#     return count
    
