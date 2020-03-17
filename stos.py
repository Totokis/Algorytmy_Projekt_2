from abc import ABC, abstractmethod

class _SizeInterface(ABC):
    @abstractmethod
    def size(self,lista)-> int:
        pass

class _IsEmptyInterface(ABC):
    @abstractmethod
    def is_empty(self,lista)-> bool:
        pass

class _PushInterface(ABC):
    @abstractmethod
    def push(self,x, lista:list)->None:
        pass

class _PopInterface(ABC):
    @abstractmethod
    def pop(self,lista:list):
        pass

class _PeekInterface(ABC):
    def peek(self,lista:list):
        pass

class IsEmpty(_IsEmptyInterface):
    def is_empty(self,lista)-> bool:
        if not lista:
            print("Pusta")
            return True
        else:
            return False
            print("Nie jest pusta")
        
class Size(_SizeInterface):
    def size(self,lista)->int:
        print(len(lista))
        return len(lista)

class Push(_PushInterface):
    def push(self, x, lista:list)->None:
        lista.append(x)
        
class Pop(_PopInterface):
    def pop(self, lista:list):

        return lista.pop()#XD, tu jest ostro Pop dziedziczy po pop by wywołać pop ale inne

class Peek(_PeekInterface):
    def peek(self, lista:list):
        return lista[-1]

class Stack:
    def __init__(self,is_empty:_IsEmptyInterface, size:_SizeInterface, 
                                push: _PushInterface, pop: _PopInterface, 
                                                peek:_PeekInterface)->None:
        self._lista = []
        self._is_empty = is_empty
        self._size = size
        self._push = push
        self._pop = pop
        self._peek = peek
    
    def is_empty(self): self._is_empty.is_empty(self._lista)
    
    def size(self): self._size.size(self._lista)

    def push(self,x): self._push.push(x,self._lista)

    def pop(self): self._pop.pop(self._lista)

    def peek(self): self._peek.peek(self._lista)

#zamiast tego powinien być container i inne pierdoły
is_empty = IsEmpty()
size = Size()
push = Push()
pop = Pop()
peek = Peek()
stack = Stack(is_empty,size,push,pop,peek)


stack.push(1)
stack.size()
