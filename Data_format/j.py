import  json
d = {
    'course':'PHP',
    'time':'2 months'
}
f = json.dumps(d)
print(f)
print(type(f))