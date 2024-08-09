import json

j = {"name":"milan","cast":"khimding","age":"27"}
file = open("new_json.json","w")
d = json.dumps(j)
hey = file.write(d)

print(type(d))
print(type(j))
print(hey)