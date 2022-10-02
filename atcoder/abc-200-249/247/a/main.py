S = input()

s = int(S, 2)
ans = str(bin(s >> 1))[2:]
while len(ans) < 4:
    ans = '0' + ans
    
print(ans)