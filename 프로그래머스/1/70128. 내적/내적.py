def solution(a, b):
    sum_ = 0
    for i in range(len(a)):
        result = a[i] * b[i]
        sum_ += result
    return sum_