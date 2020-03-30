from abc import ABC, abstractmethod, abstractproperty

class ListInterface(ABC):
    @abstractmethod
    def add(self,x): pass

    @abstractmethod
    def is_empty(self):  pass

    @abstractmethod
    def size(self)->int: pass

    @abstractmethod
    def insert(self, x, a):  pass

    @abstractmethod
    def remove(self,x):  pass

    @abstractmethod
    def remove_at(self,a):  pass

    @abstractmethod
    def find_all(self,condition):  pass

class CircularListInterface(ABC):
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
    def add(self,x,lista:CircularListInterface): pass

class IsFirst(IsFirstIntefrace):
    def is_first(self,lista:CircularListInterface): 
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
    def is_empty(self, lista: CircularListInterface): pass

class SizeInterface(ABC):
    @abstractmethod
    def size(self,lista: CircularListInterface): pass

class InsertInterface(ABC):
    @abstractmethod
    def insert(self, x, a:int, list:CircularListInterface): pass

class RemoveInterface(ABC):
    @abstractmethod
    def remove(self, lista:CircularListInterface, x): pass

class RemoveAtInterface(ABC):
    @abstractmethod
    def remove_at(self,a:int, lista:CircularListInterface): pass

class FindAllInterface(ABC):
    @abstractmethod
    def find_all(self, lista:CircularListInterface, x): pass

class FindAll(FindAllInterface):
    def find_all(self, lista:CircularListInterface, x):
        element:ElementInterface = lista.get_first()
        counter:int = 0
        indeks:int = 0
        head = element
        while element:
            if element.get_content()== x:
                counter+=1
                print(f"Element spełniający warunek: {x} o indeksie {indeks}")
                
            element = element.get_next()
            indeks+=1
            if head == element:
                break
        if not counter:
            print("Brak elementów spełniających warunki")

class RemoveAt(RemoveAtInterface):
    def __init__(self,size:SizeInterface):
        self._size = size
        
    def remove_at(self, a, lista:CircularListInterface):
        if a==0:
            x = lista.get_first()
            b = None
            while True:
                b = x
                x = x.get_next()
                if x== lista.get_first(): break
            b.set_next(x.get_next())
            return None
        element = lista.get_first()
        while a:
            element = element.get_next()
            a-=1
        element.set_next(element.get_next().get_next())
        return None

class Remove(RemoveInterface):
    def remove(self,lista:CircularListInterface):
        head:Element = lista.get_first()
        if head:
            element = head.get_next()
            head.set_next(element.get_next())
            if element == head:
                lista.set_first(None)
                del head

class Size(SizeInterface):
    def size(self, lista:CircularListInterface):
        head = lista.get_first()
        count = 0
        element = head
        while element:
            count +=1
            element = element.get_next()
            if element == head: break
        return count

class IsEmpty(IsEmptyInterface):
    def is_empty(self, lista: CircularListInterface): 
        if lista.get_first():
            print("Nie jest pusta")
            return False
        else:
            print("Jest pusta")
            return True

class Add(AddInterface):
    def __init__(self,is_first:IsFirstIntefrace): 
        self._is_first = is_first

    def add(self,x,lista:CircularListInterface):
        element = Element(x)
        head:Element = lista.get_first()
        if not head :
            element.set_next(element)
            lista.set_first(element)
        else:
            element.set_next(head.get_next())
            head.set_next(element)
            lista.set_first(element)
    
class Insert(InsertInterface):
    def __init__(self,size:SizeInterface,add: AddInterface):
        self._size = size
        self._add = add
    def insert(self, x, a:int, lista: CircularListInterface):
        new = Element(x)
        if a==0:
            head:Element = lista.get_first()
            new.set_next(head.get_next())
            head.set_next(new)
            lista.set_first(new)
            return None

        element = lista.get_first()
        while a:
            element = element.get_next()
            a-=1
        head = element
        element = new
        element.set_next(head.get_next())
        head.set_next(element)
        lista.set_first(element)

class Element(ElementInterface):
    def __init__(self,x):
        self._content = x
        self._next = None
    def __del__(self): pass

    def get_next(self): return self._next
    
    def set_next(self, next): self._next = next

    def get_content(self): return self._content

class TwoWayList(ListInterface,CircularListInterface):
    def __init__(self,add:AddInterface, is_empty: IsEmptyInterface, 
    size: SizeInterface, insert: InsertInterface, remove:RemoveInterface, remove_at: RemoveAtInterface, find_all: FindAllInterface):
        self._first:Element = None
        self._last:Element = None
        self._add = add
        self._is_empty = is_empty
        self._size = size
        self._insert = insert
        self._remove = remove
        self._remove_at = remove_at
        self._find_all = find_all

    def get_first(self): return self._first

    def get_last(self): return self._last

    def set_first(self, first): self._first = first

    def set_last(self, last): self._last = last
    
    def add(self, x) : self._add.add(x,self)

    def is_empty(self):  print(self._is_empty.is_empty(self))
    
    def size(self):  print("Ilość elementów: "+ str(self._size.size(self)))
    
    def insert(self, x, a): self._insert.insert(x,a,self)
    
    def remove(self,x):  self._remove.remove(self,x)
    
    def remove_at(self,a):  self._remove_at.remove_at(a,self)
    
    def find_all(self,condition):  self._find_all.find_all(self,condition)

    def print_from_first(self): 


        element = self.get_first()
        while element:
            element = element.get_next()
            print(element.get_content())
            if element == self.get_first():
                break


if __name__ == '__main__':
    is_first = IsFirst()
    add = Add(is_first)
    is_empty = IsEmpty()
    size = Size()
    insert = Insert(size,add)
    remove = Remove()
    remove_at = RemoveAt(size)
    find_all = FindAll()
    lista = TwoWayList(add,is_empty,size,insert,remove,remove_at,find_all)
    #!Test funkcji
    lista.add("pierwszy")
    lista.add("drugi")
    lista.add("trzeci")
    lista.insert("czwarty",0)
    lista.remove_at(2)
    lista.print_from_first()
