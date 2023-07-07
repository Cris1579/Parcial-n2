# Desarrolla una aplicación para gestionar una lista circular bidireccional de contactos telefónicos.
# Cada contacto tiene un nombre, un número de teléfono y una dirección de correo electrónico. Se
# debe implementar una lista circular bidireccional para almacenar los contactos. La lista debe
# tener las siguientes funcionalidades. Debe contener las siguientes funciones:
# A. Clases respectivas del problema
# B. Método para agregar un contacto a la lista
# C. Método para mostrar la lista de contactos
# D. Método para buscar un contacto por su nombre
# E. Método eliminar un contacto de la lista
# F. Método para verificar si la lista de contacto está vacía

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
            nuevo_nodo.next = self.head
        else:
            actual = self.head
            while actual.next != self.head:
                actual = actual.next
            actual.next = nuevo_nodo
            nuevo_nodo.next = self.head

    def eliminar(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            actual = self.head
            while actual.next != self.head:
                actual = actual.next
            actual.next = self.head.next
            self.head = self.head.next
        else:
            actual = self.head
            prev = None
            while actual.next != self.head:
                prev = actual
                actual = actual.next
                if actual.data == data:
                    prev.next = actual.next
                    actual = actual.next

    def mostrar(self):
        if self.head is None:
            return
        actual = self.head
        while actual.next != self.head:
            print(actual.data, end=' ')
            actual = actual.next
        print(actual.data)

    def exist(self, data):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                return False

    def vacio(self):
        if self.head is None:
            print("La lista esta vacía")
        else:
            print("La lista no esta vacía")