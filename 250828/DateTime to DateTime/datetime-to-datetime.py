a, b, c = map(int, input().split())

# Please write your code here.
if a>=11 and b>=11 and c>=11:
    a-=11
    b-=11
    c-=11
    print(a*24*60 + b*60 + c)

else:
    print(-1)