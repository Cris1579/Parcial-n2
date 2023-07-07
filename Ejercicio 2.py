# Desarrolla un sistema de gestión de inventario utilizando listas bidireccionales. Cada artículo del
# inventario tiene un código único, un nombre, una descripción y una cantidad disponible. El
# sistema debe realizar las siguientes operaciones:
# A. Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad
# inicial
# B. Eliminar un artículo del inventario utilizando su código
# C. Buscar un artículo en específico por su código
# D. Actualizar la cantidad disponible de un artículo
# E. Mostrar todos los artículos del inventario en orden ascendente según su código

class Nodo:
    def __init__(self,id,name,desc,cantidad):
        self.back = None
        self.next = None
        self.id = id
        self.name = name
        self.descripcion = desc
        self.cantidad = cantidad

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def EstaVacioFun(self):
        return self.primero is None

    def EstaVacio(self):
        if self.primero is None:
            return "Esta vacío"
        else: return "No esta vacío"

    def agregar(self,id,name,desc,cantidad):
        nuevo_nodo = Nodo(id,name,desc,cantidad)
        if self.EstaVacioFun():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.back = self.ultimo
            self.ultimo.next = nuevo_nodo
            self.ultimo = nuevo_nodo

    def existe(self,buscar): #Por si quisiera implementar un menú
        actual = self.primero
        while actual:
            if actual.id == buscar:
                return True
            actual = actual.next
        return False

    def eliminar(self,buscar):
        actual = self.primero
        while actual is not None:
            if actual.id == buscar:
                if actual.back is not None:
                    actual.back.next = actual.next
                else:
                    self.primero = actual.next
                if actual.next is not None:
                    actual.next.back = actual.next
                else:
                    self.ultimo = actual.back
                return True
            actual = actual.next
        return False

    def buscar(self,id):
        actual = self.primero
        while actual is not None:
            if actual.id == id:
                return actual
            actual = actual.next
        return None

    def imprimir_ascend(self):
        nodos = []
        actual = self.primero
        while actual is not None:
            nodos.append(actual)
            actual = actual.next
        nodos.sort(key=lambda x: x.id)
        for nodo in nodos:
            print(f'Codigo : {nodo.id},Descripción: {nodo.descripcion}, Cantidad: {nodo.cantidad}')

    def actualizar(self,id,newCant):
        actual = self.primero
        while actual is not None:
            if actual.id == id:
                actual.cantidad = newCant
                return True
            actual = actual.next
        return False


listaArt = ListaDoble()
#Agregando articulos
# Ejemplo: Articulo = listaArt.agregar("id","nombre del articulo","Descripcion","cantidad")
articulo_1 = listaArt.agregar("4763","Lampara","Lampara de mesa","2")
articulo_2 = listaArt.agregar("7834","Pc gamer","Computadora","5")
articulo_3 = listaArt.agregar("1234","Sarten","Sarten de cocina","8")

#Buscando un articulo
#ejemplo
buscar = listaArt.buscar("4763")
if buscar is not None:
    print("Articulo Encontrado")
    print(f'Id: {buscar.id},Descripción: {buscar.descripcion}, cantidad: {buscar.cantidad}')
else:
    print("Articulo no encontrado")

#segundo ejemplo
# buscar.listaArt.buscar("9999")
# Saldrá 'Articulo no encontrado'


#Actualizando un articulo
nueva_cantidad = listaArt.actualizar("4763","10")

#Imprimiendo los articulos
print("\nLista de todos los artículos")
listaArt.imprimir_ascend()

#ELiminando un articulo
#De este modo, se elimina un articulo que
delete = listaArt.eliminar("7834")


#Imprimiendo otra vez los articulos
print("\nLista nueva de articulos")
listaArt.imprimir_ascend()

