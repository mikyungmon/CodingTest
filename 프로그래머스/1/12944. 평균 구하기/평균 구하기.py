def solution(arr):
    sum = 0
    avg = 0
    for i in range(len(arr)):
        sum += arr[i]
        
    avg = sum / len(arr)
    
    return avg