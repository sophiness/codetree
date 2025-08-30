a, b = map(int, input().split())
n = input()

# Please write your code here.
num = 0
for i in n:
    num = num*a+int(i)

ans = ''
while num>0:
    ans = str(num%b) +ans
    num//=b

print(ans)