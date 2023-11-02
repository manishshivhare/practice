
listq = [1, 0 , 1,1,0,1,0,0]
listm = [0,1,1,1,1]
lista = [0,0,0,0,0]
def shiftleft(lista, listq):
    temp = listq[0]
    for index, a in enumerate(listq):
        listq[index] = listq[index+1]
    listq[-1] = 0
    for index,a in enumerate(lista):
        lista[index] = lista[index+1]
    lista[-1] = temp
def merge(lista, listm):
    for i in range (len(lista)):
        lista[i] = bin(lista[i] + listm[i])
for i in range(8):
    shiftleft(lista, listq)
    merge(lista, listm)

    