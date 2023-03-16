numeros = [10,20,30,40,50]

maior_numero = numeros[0] #inicializando a váriaveis que irá armazenar o maior número

for numero in numeros: # usando um loop for para percorrer a lista e encontrar o maior número
    if numero > maior_numero: 
        maior_numero = numero

print("O maior número da lista é: ", maior_numero)