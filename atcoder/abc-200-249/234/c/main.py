K = int(input())

bin_k = str(bin(K))
print(bin_k[2:].replace('1', '2'))