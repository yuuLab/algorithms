N = int(input())

ans = 0
n = 11
while n <= N:
    if len(str(n)) % 2 != 0:
        n *= 10
    else:
        str_n = str(n)
        center = len(str_n) // 2
        if str_n[:center] == str_n[center:]:
            ans += 1
            temp = n + 10**center
            if len(str(temp)) > len(str_n):
                n += 1
            else:
                n = temp
            continue
        n += 1
        
print(ans)

# 公式回答
'''
条件を満たす整数はAAABBBと表記されたときに、AAA=BBBとなるものとなっている。
条件を満たす整数を効率良く全列挙したいと考えたときに、片方だけ全列挙すればもう片方はその値で確定してしまう。
よって、10**12桁の数があったとしても後半だけを全列挙すればいいので、10**6通りの全列挙にすることができた。
あとは、後半から前半を作って、数xを作った後、N以下であるものを判定していけばいい。
後半部分から数xを作る部分が少し面倒なのだが、多少計算量をサボっても問題ない。

N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2 > N):
        print(i - 1)
        exit()
'''
