n = int(input())

# Please write your code here.
# digits = []
# while True:
#     if n<2:
#         digits.append(n)
#         break

#     digits.append(n%2)
#     n //= 2

# for digit in digits[::-1]:
#     print(digit, end = '')


result = ''
while n>0:
    result = str(n%2)+result
    n //= 2

print(result)