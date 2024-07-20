d= {
    'name': 'Milan',
    'surname': 'Khimding',
    'age': '27',
    'address': 'Kerabari'
}
n = d.get('name')
print(d['name'],n)
print()

for n in d.keys():
    print(n)
print()
for n in d.values():
    print(n)
print()
for a,b in d.items():
    print(a,b)

# del d['name']
# print(d)
#

# e = d.pop('name')
#
# print(d)
# print(e)

f = dict(name="Jamin",fees = '2000')
f.update({'fees': 1000,'age': 30})
print(f)