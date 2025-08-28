a, b, c = map(int, input().split())

# Please write your code here.

dt2 = a*24*60 + b*60 + c
dt1 = 11*24*60 + 11*60 + 11

ans = dt2 - dt1
if ans>=0:
    print(ans)
else:
    print(-1)
