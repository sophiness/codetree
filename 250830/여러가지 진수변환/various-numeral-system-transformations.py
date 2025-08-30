N, B = map(int, input().split())

# Please write your code here.

def converter(n,b):
    digits = []
    while True:
        if n<b:
            digits.append(n)
            break
        digits.append(n%b)
        n //= b
    for digit in digits[::-1]:
        print(digit, end = '')

converter(N,B)
            