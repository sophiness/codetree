n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0]*200
for x1,x2 in segments:
    for i in range(x1,x2):
        x1+=100
        x2+=100
        line[i] += 1
print(max(line))
