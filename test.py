import sys
input = sys.stdin.readline

n = int(input())
people = []

# 입력 받기
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

# 각 사람의 등수 계산
ranks = []
for i in range(n):
    rank = 1  # 기본 1등
    for j in range(n):
        if i == j:  # 자기 자신은 제외
            continue
        # 둘 다 작으면 등수 +1
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

# 출력
print(' '.join(map(str, ranks)))