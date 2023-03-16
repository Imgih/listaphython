lista_com_duplicatas = [1,2,3,1,4,2,5,6,3,7,8,5,9]

lista_sem_duplicatas = []

while lista_com_duplicatas:# usando um loop while para percorrer a lsita e remover os elementos duplicados
    elemento = lista_com_duplicatas.pop(0) # pop é usado para remover elementos
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
print("A lista sem duplicatas é: ", lista_sem_duplicatas)