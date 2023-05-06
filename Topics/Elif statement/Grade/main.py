x = int(input())
y = int(input())
c = y/100
d = x/c
if d < 60:
    print('F')
elif 90 <= d and d <= 100:
    print('A')
elif 80 <= d and d < 90:
    print('B')
elif 70 <= d and d < 80:
    print('C')
elif 60 <= d and d < 70:
    print('D')

