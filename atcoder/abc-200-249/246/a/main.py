x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ans_x = 0
ans_y = 0
if x1 == x2:
    ans_x = x3
elif x2 == x3:
    ans_x = x1
else:
    ans_x = x2

if y1 == y2:
    ans_y = y3
elif y2 == y3:
    ans_y = y1
else:
    ans_y = y2
    
print(ans_x, ans_y)