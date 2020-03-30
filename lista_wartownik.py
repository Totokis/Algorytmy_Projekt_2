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

class SentryListInterface(ABC):
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
    def add(self,x,lista:SentryListInterface): pass

class IsFirst(IsFirstIntefrace):
    def is_first(self,lista:SentryListInterface): 
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
    def is_empty(self, lista: SentryListInterface): pass

class SizeInterface(ABC):
    @abstractmethod
    def size(self,lista: SentryListInterface): pass

class InsertInterface(ABC):
    @abstractmethod
    def insert(self, x, a:int, list:SentryListInterface): pass

class RemoveInterface(ABC):
    @abstractmethod
    def remove(self, lista:SentryListInterface, x): pass

class RemoveAtInterface(ABC):
    @abstractmethod
    def remove_at(self,a:int, lista:SentryListInterface): pass

class FindAllInterface(ABC):
    @abstractmethod
    def find_all(self, lista:SentryListInterface, x): pass

class FindAll(FindAllInterface):
    def find_all(self, lista:SentryListInterface, x):
        #!Zmiana funkcji find all na wersję by pokazać działanie wartownika
        sentry = Element(x)
        lista.get_last().set_next(sentry)
        element:ElementInterface = lista.get_first()
        indeks = 0
        while element:
            if element ==  sentry:
                print("Brak elemetu")
                lista.get_last().set_next(None)
                return None
            elif element.get_content() == x: 
                print(f"Element o indeksie {indeks}")
                return None
            element = element.get_next()
        

class RemoveAt(RemoveAtInterface):
    def __init__(self,size:SizeInterface):
        self._size = size
        
    def remove_at(self, a, lista:SentryListInterface):
        size:int = self._size.size(lista)
        if size <= a:
            print("za duza wartość")
            return None
        else:
            element:ElementInterface = lista.get_first()
            if a == 0:
                lista.set_first(element.get_next())
                del element
                return None

            element_previous:ElementInterface = None
            while True:
                if a:
                    element_previous = element
                    element = element.get_next()
                    a-=1
                else:
                    element_previous.set_next(element.get_next())
                    del element
                    break

class Remove(RemoveInterface):
    def remove(self,lista:SentryListInterface, x):
        element = lista.get_first()
        previous:ElementInterface = None
        if element.get_content() == x:
            replace = element.get_next()
            #destruktor elementu
            del element
            lista.set_first(replace)
            return None

        while element:
            if str(element.get_content()) == str(x):
                replace = element.get_next()
                element.set_next(None)
                del element
                #print("destruktor elementu")
                previous.set_next(replace)
                return None
            previous = element
            element = element.get_next()
        print("Nie ma takiego elementu")

class Size(SizeInterface):
    def size(self, lista:SentryListInterface):
        count = 0
        element = lista.get_first()
        while element:
            count +=1
            print("--"+element.get_content()+"--")
            element = element.get_next()
        return count

class IsEmpty(IsEmptyInterface):
    def is_empty(self, lista: SentryListInterface): 
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
    def __del__(self):
        pass
        #print(f"Element {self._content} został usunięty")

    def get_next(self): return self._next
    
    def set_next(self, next): self._next = next

    def get_content(self): return self._content

class Add(AddInterface):
    def __init__(self,is_first:IsFirstIntefrace): 
        self._is_first = is_first

    def add(self,x,lista:SentryListInterface):
        if self._is_first.is_first(lista):
            #print("is first")
            element = Element(x)#stwórz element
            last = lista.get_last()#wyślij jego adres do poprzedniego elementu
            last.set_next(element)
            #print("Tutaj")
            lista.set_last(element)#ustaw ten element jako ostatni
        else:
            element = Element(x)
            lista.set_first(element)
            lista.set_last(element)

class Insert(InsertInterface):

    def __init__(self,size:SizeInterface,add: AddInterface):
        self._size = size
        self._add = add
    def insert(self, x, a:int, list:SentryListInterface):
        if a >= self._size.size(list):
            self._add.add(x,lista)
        elif self._size.size(list) == a:
            self._add.add(x,lista)
        else:
            new = Element(x)
            element = list.get_first()
            element_previous = None
            while True:
                if a:
                    element_previous = element
                    element = element.get_next()
                    a-=1
                else:
                    new.set_next(element)
                    if element_previous: element_previous.set_next(new)
                    break

class SentryList(ListInterface,SentryListInterface):
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

if __name__ == '__main__':
    is_first = IsFirst()
    add = Add(is_first)
    is_empty = IsEmpty()
    size = Size()
    insert = Insert(size,add)
    remove = Remove()
    remove_at = RemoveAt(size)
    find_all = FindAll()
    lista = SentryList(add,is_empty,size,insert,remove,remove_at,find_all)
    
    #!Test funkcji 