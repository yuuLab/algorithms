N = int(input())
# setを使用して重複は減らす、[in]で検索時の計算量削減
S = set(input() for i in range(N))

exist = False
for s in S:
    if '!' + s in S:
        print(s)
        exist = True
        break
            
if not exist:
    print('satisfiable')