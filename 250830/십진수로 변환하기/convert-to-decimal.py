binary = input()

# Please write your code here.
n = 0
binary = list(map(int, list(binary)))
for i in binary:
    n = n*2+i

print(n)