x1, y1, x2, y2 = map(int, input().split())

targets = []
for i in range(3):
    for j in range(3):
        targets.append([x1+i, y1+j])
        targets.append([x1+i, y1-j])
        targets.append([x1-i, y1+j])
        targets.append([x1-i, y1-j])
        targets.append([x2+i, y2+j])
        targets.append([x2+i, y2-j])
        targets.append([x2-i, y2+j])
        targets.append([x2-i, y2-j])
    
ans = [0 for _ in range(len(targets))]
for i in range(len(targets)):
    t = (x1 - targets[i][0])**2 + (y1 - targets[i][1])**2
    if t == 5:
        ans[i] += 1
        
for i in range(len(targets)):
    t = (x2 - targets[i][0])**2 + (y2 - targets[i][1])**2
    if t == 5:
        ans[i] += 1

output = 'No'
for a in ans:
    if a == 2:
        output = 'Yes'
        break
print(output)