n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
block = [0]*n
for a,b in commands:
    for i in range(a,b+1):
        block[i] += 1

print(max(block))