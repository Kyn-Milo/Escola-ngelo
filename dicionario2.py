pais = {'nome' : 'Brasil', 'capital' : 'Brasília'}

print(pais)

print(pais['capital'])

pais.clear()

print(pais)

#Método get()
print(pais.get('nome'))
print(pais.get("qualquer", "não existe"))