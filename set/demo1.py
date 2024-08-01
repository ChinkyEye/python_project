s = {1,2,3,1}
l = [10,20,30]

print(s)
for a in s:
    print(a)

change_set = set(l)
print(change_set)
change_set.add(40)
print(change_set)

#pop random element from set
change_set.pop()
# print(change_set.pop())
print(change_set)

#remove elements
change_set.remove(10)
print(change_set)

#decard elements
change_set.discard(20)
print(change_set)

#clear elements
change_set.clear()
print(change_set)

#update elements
s.update(l)
print(s)


