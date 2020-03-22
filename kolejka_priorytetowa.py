from abc import ABC, abstractmethod

class _Sort:
    def sort(self,_lista,head,tail):
        lista = _lista
        #print(f"ListaAB: {lista}")
        lista_A = lista[tail:]
        lista_B = lista[:tail]
        #print(f"Lista A :{lista_A}")
        #print(f"Lista B : {lista_B}")
        lista = lista_A + lista_B
        #print(f"Lista: {lista}")
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                a = lista[j]
                b = lista[j+1]
                #print(f"->{a[1]}, ->{b[1]}")
                if (a[1] > b[1]):
                    lista[j], lista[j+1] = lista[j+1],lista[j]
        #print(f"Lista_2: {lista}")

        lista_A = lista[:-tail]
        lista_B = lista[-tail:]
        lista = lista_B + lista_A
        #print(f"Lista A 2:{lista_A}")
        #print(f"Lista B 2: {lista_B}\n #######################")
        return lista
#
class _ReplaceLast:
    def replace_last(self,tail,limit):
        print("za duzo elementów")
        if tail == 0:
            tail = limit-1
            return tail
        else:
            tail = tail - 1
            return tail
#
class _IsFull():
    def is_full(self,lista):
        licznik = 0
        for element in lista:
            if element == [0,0]:
                licznik = licznik + 1
        if licznik==0:
            return True
        else:
            return False
#
class _HeadIncrement():
    def head_increment(self,head,limit):
        if head == limit-1:
            return 0 
        else:
            return head+1
#
class _TailIncrement:
    def tail_increment(self,tail,limit):
        if tail == limit-1:
            return 0
        else:
            return tail+1
        
#
class Stack():
    def __init__(self,limit, tail_increment: _TailIncrement):
        self._lista=[]
        self._limit = limit
        #*Zapełnienie listy#TODO zmienić na NULL
        for i in range(self._limit):
            element = [0,0]
            self._lista.append(element)
        self._head = 0
        self._tail = 0
        self._is_full = _IsFull()
        self._tail_increment = _TailIncrement()
        self._head_increment = _HeadIncrement()
        self._replace_last = _ReplaceLast()
        self._sort = _Sort()

    def size(self):
        licznik = 0
        for element in self._lista:
            if element != 0:
                licznik+=1
        print(f"W kolejce jest {licznik} / {self._limit} elementów")

    def is_empty(self):
        licznik = 0
        for element in self._lista:
            if element == 0:
                licznik = licznik + 1
        if licznik!=0:
            print("Kolejka jest pusta")
            return True
        else:
            print("Kolejka posiada elementy")
            return False

    def print_content(self):
        print(self._lista)
        print(f"Head: {self._head} oraz tail: {self._tail}")

    def clear_buffer(self):
        for i in range(self._limit):
            self._lista.append(0)

    def enqueue(self, element,key):
        full_element = [element,key]
        if self._is_full.is_full(self._lista):
            self._tail = self._replace_last.replace_last(self._tail,self._limit)
            self._lista[self._tail] = [element,key]
            self._tail = self._tail_increment.tail_increment(self._tail, self._limit)
            self._lista = self._sort.sort(self._lista,self._head,self._tail)
        else:
            self._lista[self._tail] = full_element
            self._tail = self._tail_increment.tail_increment(self._tail, self._limit)
            self._lista = self._sort.sort(self._lista,self._head,self._tail)
#
    def dequeue(self):
        element = self._lista[self._head]
        self._lista[self._head] = [0,0]
        self._head = self._head_increment.head_increment(self._head,self._limit)
        #self._lista = self._sort.sort(self._lista)
        return element

    def peek(self):
        element = self._lista[self._head]
        print(f"Pierwszy element to {element}")
        return element


