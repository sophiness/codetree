n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
block = [0]*200
idx = 99

for i in range(n):
    
    if dir[i] == 'R':
        for j in range(x[i]):
            block[idx] += 1
            idx += 1
    elif dir[i] == 'L':
        for k in range(x[i]):
            block[idx] += 1
            idx -= 1
ans = 0
for b in block:
    if b>=2:
        ans+=1

print(ans)

    