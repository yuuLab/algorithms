S = input()
end = len(S) - 1

# 先頭のaの個数
count = 0
for i in range(0, len(S)):
    if S[i] != 'a':
        count = i + 1
        break

for i in reversed(range(0, len(S))):
    if S[i] != 'a':
        end = i
        break
target = S[0:min(end+count, len(S))]

if target == target[::-1]:
    print('Yes')
else:
    print('No')