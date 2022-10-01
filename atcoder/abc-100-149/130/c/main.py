W, H, x, y = map(int, input().split())

# 長方形の中心を通るように直線を引いたときに面積は最大になる。（長方形の面積の半分）。
# x=2/W, y=2/Hだった場合、直線は複数ありえて、それ以外だと一意になる。
if 2*x == W and 2*y == H:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)
