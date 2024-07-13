l1= [ ]
for a in range(1,10): # normal append
    l1.append(a)


# comprehension

l2 = [n for n in range(1,10) if n%2== 0]

print(l2)
print(l1)