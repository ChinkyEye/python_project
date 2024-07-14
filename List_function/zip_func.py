l1 = [1, 2, 3, 4]
l2 = [10, 11, 12, 13]

for a,b in zip(l1,l2):
    print(a,b)

length = len(l1)
print(length)

for h in range(length):
    print(l1[h],l2[h])