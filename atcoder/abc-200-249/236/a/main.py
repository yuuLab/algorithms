S = input()
a, b = map(int, input().split())

tmp_a = S[a-1]
tmp_b = S[b-1]
print(S[:a-1] + tmp_b + S[a:b-1] + tmp_a + S[b:])