minha_lista = [1,2,3,4,5] #criando uma lista

for i in range (len(minha_lista)): # usando um loop for para percorrer a lista e imprimir cada elemento
    print("O elemento",i+1, "da lista é:", minha_lista[i] )

numeros = [1,2,3,4,5]

for numero in numeros: #usando um loop for para percorrer a lista e imprimir cada elemento
    print(numero, "- com for")

i = 0 #usando um loop while para percorrer a lista e imprimir cada elemento
while i < len(numeros):
    print(numeros[i], " - Com while")
    i += 1

    