import sys

# 입력을 한 번에 받기
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

numbers.sort()

# 출력 최적화: 한 번에 출력
sys.stdout.write("\n".join(map(str, numbers)) + "\n")