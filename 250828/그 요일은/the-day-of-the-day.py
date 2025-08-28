m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

days_of_week = ['','Tue','Wed','Thu','Fri','Sat','Sun','Mon']
A = days_of_week.index(A)
A = int(A)

def num_of_days(m,d):
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,m):
        m+=days[i]
    return m+d

diff = num_of_days(m2,d2)-num_of_days(m1,d1)+A
print(diff//7)

