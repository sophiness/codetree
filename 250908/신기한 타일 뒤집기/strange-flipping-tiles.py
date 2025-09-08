n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
tiles = ['']*2*sum(x)
idx = sum(x)
for i in range(n):
    if dir[i]=='R':
        for j in range(x[i]):
            tiles[idx] = 'B'
            if j != x[i]-1:
                idx+=1
    else:
        for _ in range(x[i]):
            tiles[idx] = 'W'
            if j != x[i]-1:
                idx-=1

print(tiles.count('W'), tiles.count('B'))