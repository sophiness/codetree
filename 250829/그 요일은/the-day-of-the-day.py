m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

days_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
A = days_of_week.index(A)
A = int(A)

def num_of_days(m,d):
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,m):
        m+=days[i]
    return m+d

diff = num_of_days(m2,d2)-num_of_days(m1,d1)+1
if diff%7>A:
    print(diff//7+1)
else:
    print(diff//7)

