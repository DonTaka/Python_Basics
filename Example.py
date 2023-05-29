#Crear Lista
lista = [1,5,25,100,500]
print("Inicial: ",lista)

#Append()=Agregar un dato al final de la lista
lista.append(250)
print("Append:  ",lista)

#Extend([]) = Toma una segunda lista y agrega sus datos a la primera en la ultima posicion
lista2 = [75,125]
lista.extend(lista2)
print("Extend:  ",lista)

#Insert(posicion,valor) = Agregamos dato en la posicion indicada
lista.insert(2,400)
print("Insert:  ",lista)

#Remove(valor) = Busca y elimina el dato entregado
lista.remove(400)
print("Remove:  ",lista)

#Pop() = Elimina el ultimo registro
#Pop(Posicion) = Elimina la posicion entregada
lista.pop()
print("Pop:     ",lista)
lista.pop(2)
print("Pop(2):  ",lista)

#Reverse = Invierte el orden de la Lista
lista.reverse()
print("Reverse: ",lista)

#Sort = Ordenar De menor a mayor
lista.sort()
print("Sort:    ",lista)

#Sort(Reverse=True) = Ordena de mayor a menor
lista.sort(reverse=True)
print("Sort(r): ",lista)