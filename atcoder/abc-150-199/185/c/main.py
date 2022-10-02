from scipy.special import comb
# comb : combination1が使用可能　引数exact=Falseで浮動小数店数Floatが返される。Trueの場合、整数intで返される

L = int(input())
ans = comb(L - 1, 11, exact=True)
print(ans)