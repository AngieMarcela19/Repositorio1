import json
#leer archivo ---> abrirlo
f= open("dict.json", "r")
c= f.read()
#print(c)
js= json.loads(c)
#print(js)
print(js['toni'])