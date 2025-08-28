m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

days = [31,28,31,30,31,30,31,31,30,31,30,31]

md1 = 0
md2 = 0
for i in range(m2-1):
    md2 += days[i]
for j in range(m1-1):
    md1 += days[j]

md2 += d2
md1 += d1

print(md2-md1+1)
