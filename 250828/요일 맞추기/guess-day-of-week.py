m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

d = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

m = [31,28,31,30,31,30,31,31,30,31,30,31]

md1 = 0
md2 = 0

for i in range(m1-1):
    md1+=m[i]
md1+=d1
for j in range(m2-1):
    md2+=m[j]
md2+=d2

print(d[(md2-md1)%7])