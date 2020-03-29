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
    def is_first(self,lista:OneWayListInterface): 
        if lista.get_first() != None:
            return True
            print("tutaj")
        else:
            return False

class ElementInterface(ABC):
    @abstractmethod
    def __init__(self,x):pass

    @abstractmethod
    def get_next(self): pass

    @abstractmethod
    def set_next(self, next): pass

    @abstractmethod
    def get_content(self): pass

class IsEmptyInterface(ABC):
    @abstractmethod
    def is_empty(self, lista: OneWayListInterface): pass

class SizeInterface(ABC):
    @abstractmethod
    def size(self,lista: OneWayListInterface): pass

class InsertInterface(ABC):
    @abstractmethod
    def insert(self, x, a:int, list:OneWayListInterface): pass

class Insert(InsertInterface):
    def insert(self, x, a:int, list:OneWayListInterface):
        count = a
        element = lista.get_first()
        while element and count<:
            count +=1
            element = element.get_next()

class Size(SizeInterface):
    def size(self, lista:OneWayListInterface):
        count = 0
        element = lista.get_first()
        while element:
            count +=1
            element = element.get_next()

        print(f"Ilość elementów to {count}")

class IsEmpty(IsEmptyInterface):
    def is_empty(self, lista: OneWayListInterface): 
        if lista.get_first():
            print("Nie jest pusta")
            return False
        else:
            print("Jest pusta")
            return True

class Element(ElementInterface):
    def __init__(self,x):
        self._content = x
        self._previous = None
        self._next = None

    def get_next(self): return self._next
    
    def set_next(self, next): self._next = next

    def get_content(self): return self._content

class Add(AddInterface):
    def __init__(self,is_first:IsFirstIntefrace): 
        self._is_first = is_first

    def add(self,x,lista:OneWayListInterface):
        if self._is_first.is_first(lista):
            print("is first")
            element = Element(x)#stwórz element
            last = lista.get_last()#wyślij jego adres do poprzedniego elementu
            last.set_next(element)
            lista.set_last(element)#ustaw ten element jako ostatni
        else:
            element = Element(x)
            lista.set_first(element)
            lista.set_last(element)

class OneWayList(ListInterface,OneWayListInterface):
    def __init__(self,add:AddInterface, is_empty: IsEmptyInterface, size: SizeInterface):
        self._first:Element = None
        self._last:Element = None
        self._add = add
        self._is_empty = is_empty
        self._size = size
    
    def get_first(self): return self._first

    def get_last(self): return self._last

    def set_first(self, first): self._first = first

    def set_last(self, last): self._last = last
    
    def add(self, x) : self._add.add(x,self)

    def is_empty(self):  print(self._is_empty.is_empty(self))
    
    def size(self):  self._size.size(self)
    
    def insert(self, x, a):  pass
    
    def remove(self,x):  pass
    
    def remove_at(self,a):  pass
    
    def find_all(self,condition):  pass

    def print_all(self): pass

if __name__ == '__main__':
    lista = OneWayList(add=Add(is_first=IsFirst()),is_empty=IsEmpty(),size=Size())
    lista.add("wasup")
    lista.add("next")
    print(lista.get_first().get_content())
    print(lista.get_last().get_content())
    lista.is_empty()
    lista.size()
    lista.add("hmm")
    lista.size()
    #!test komentarza