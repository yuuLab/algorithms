from collections import Counter

S = input()
if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else: 
        print('No')
    exit()
    
cnt = Counter(S)
for i in range(112, 1000, 8):
    if not Counter(str(i)) - cnt:
        print('Yes')
        exit()
print('No')