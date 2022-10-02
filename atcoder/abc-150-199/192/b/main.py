S = input()

index = 0
for i in S:
    if index % 2 == 0:
        if not i.islower():
            print('No')
            exit()
    else:
        if i.islower():
            print('No')
            exit()
    index += 1
print('Yes')