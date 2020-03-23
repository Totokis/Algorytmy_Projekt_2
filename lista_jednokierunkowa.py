from abc import ABC, abstractmethod, abstractproperty

class ListInterface(ABC):
    @abstractmethod
    def add(self,x): pass

    @abstractmethod
    def is_empty(self):  pass

    @abstractmethod
    def size(self):  pass

    @abstractmethod
    def insert(self, x, a):  pass

    @abstractmethod
    def remove(self,x):  pass

    @abstractmethod
    def remove_at(self,a):  pass

    @abstractmethod
    def find_all(self,condition):  pass

class OneWayListInterface(ABC):
    @abstractmethod
    def get_first(self): pass

    @abstractmethod
    def get_last(self): return Element

    @abstractmethod
    def set_first(self, first): pass

    @abstractmethod
    def set_last(self, last): pass

class IsFirstIntefrace(ABC):
    @abstractmethod
    def is_first(self, lista)->bool:   pass

class AddInterface(ABC):
    @abstractmethod
    def add(self,x,lista:OneWayListInterface): pass

class IsFirst(IsFirstIntefrace):
    def is_first(self,lista:OneWayListInterface): True if lista.get_first() else False

class ElementInterface(ABC):
    @abstractmethod
    def __init__(self,x):pass

    @abstractmethod
    def get_next(self): pass

    @abstractmethod
    def set_next(self): pass

    @abstractmethod
    def get_content(self): pass

class IsEmptyInterface(ABC):
    @abstractmethod
    def is_empty(self, lista: OneWayListInterface): pass

class IsEmpty(IsEmptyInterface):
    def is_empty(self, lista: OneWayListInterface): True if lista.get_first() else False

class Add(AddInterface):
    def __init__(self,is_first:IsFirstIntefrace): 
        self._is_first = is_first

    def add(self,x,lista:OneWayListInterface):
        if self._is_first.is_first(lista):
            element = Element(x)#stwórz element
            last = lista.get_last()#wyślij jego adres do poprzedniego elementu
            last.set_next(element)
            lista.set_last(element)#ustaw ten element jako ostatni
        else:
            element = Element(x)
            lista.set_first(element)
            lista.set_last(element)

class Element(ElementInterface):
    def __init__(self,x):
        self._content = x
        self._previous = None
        self._next = None

    def get_next(self): return self._next
    
    def set_next(self,next): self._next = next

    def get_content(self): return self._content

class OneWayList(ListInterface,OneWayListInterface):
    def __init__(self,add:AddInterface):
        self._first:Element = None
        self._last:Element = None
        self._add = add
    
    def get_first(self): return self._first

    def get_last(self): return self._first

    def set_first(self, first): self._first = first

    def set_last(self, last): self._last = last
    
    def add(self, x) : self._add.add(x,self)

    def is_empty(self):  pass
    
    def size(self):  pass
    
    def insert(self, x, a):  pass
    
    def remove(self,x):  pass
    
    def remove_at(self,a):  pass
    
    def find_all(self,condition):  pass

    def print_all(self): pass

if __name__ == '__main__':
    lista = OneWayList(add=Add(is_first=IsFirst()))
    lista.add("wasup")
    lista.add("next")
    print(lista.get_first().get_content())
    print(lista.get_last().get_content())