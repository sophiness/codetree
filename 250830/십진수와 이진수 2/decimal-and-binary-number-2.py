N = input()

# Please write your code here.
N = list(map(int,list(N)))
n = 0
for i in N:
    n = n*2+i

n *= 17

digits = []
while True:
    if n<2:
        digits.append(n)
        break
    digits.append(n%2)
    n//=2

for digit in digits[::-1]:
    print(digit,end='')
