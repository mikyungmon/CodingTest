def solution(arr):
    answer = []
    for i in range(len(arr)):
        if (len(answer) == 0) & (arr[i] not in answer):
            answer.append(arr[i])
        elif (len(answer)!= 0) & (arr[i] != answer[-1]):
            answer.append(arr[i])
    return answer
           