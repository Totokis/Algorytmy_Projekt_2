from abc import ABC, abstractmethod

class _QueueInterface(ABC):
    @abstractmethod
    def is_empty(self,lista:list): pass

    @abstractmethod
    def size(self,lista:list): pass

    @abstractmethod
    def enqueue(self,x,lista:list): pass

    @abstractmethod
    def dequeue(self,lista:list): pass

    @abstractmethod
    def peek(self,lista:list): pass

class _IsEmptyInterface(ABC):
    @abstractmethod
    def is_empty(self,lista:list): pass

class _SizeInterface(ABC):
    @abstractmethod
    def size(self,lista:list,limit:int): pass

class _EnqueueInterface(ABC):
    @abstractmethod
    def enqueue(self, x, lista:list, tail:int, limit:int): pass

class _DequeueInterface(ABC):
    @abstractmethod
    def dequeue(self, lista:int, head:int, limit:int): pass

class _PeekInterface(ABC):
    @abstractmethod
    def peek(self,lista:list): pass

class _PrintContentInterface(ABC):
    @abstractmethod
    def print_content(self,lista:list, head:int, tail:int): pass

class _ClearBufferInterface(ABC):
    @abstractmethod
    def clear_buffer(self,limit:int): pass

class _ReplaceLastInterface(ABC):
    @abstractmethod
    def replace_last(self,tail:int,limit:int): pass

class _IsFullInterface(ABC):
    @abstractmethod
    def is_full(self,lista:list): pass

class _HeadIncrementInterface(ABC):
    @abstractmethod
    def head_increment(self,head:int,limit:int): pass

class _TailIncrementInterface(ABC):
    @abstractmethod
    def tail_increment(self,tail:int,limit:int): pass


class IsEmpty(_IsEmptyInterface):
    def is_empty(self, lista):   
        licznik = 0
        for element in lista:
            if element == 0: licznik = licznik + 1
        if licznik:
            print("Kolejka jest pusta")
            return True
        else:
            print("Kolejka posiada elementy")
            return False

class Size(_SizeInterface):
    def size(self, lista,limit):
        licznik = 0
        for element in lista:
            if element: licznik+=1
        print(f"W kolejce jest {licznik} / {limit} elementów")

class Enqueue(_EnqueueInterface):
    def __init__(self, is_full: _IsFullInterface,replace: _ReplaceLastInterface, 
    tail_increment:_TailIncrementInterface):
        self._is_full = is_full
        self._replace = replace
        self._tail_increment = tail_increment
        
    def enqueue(self, x, lista:list, tail:int, limit:int):
        if self._is_full.is_full(lista):
            tail = self._replace.replace_last(tail,limit)
            lista[tail] = x
            tail = self._tail_increment.tail_increment(tail,limit)
            # def print_alert(self): pass
        else:
            lista[tail] = x
            tail = self._tail_increment.tail_increment(tail, limit)

class Dequeue(_DequeueInterface):
    def __init__(self, head_increment: _HeadIncrementInterface):
        self._head_increment = head_increment

    def dequeue(self, lista:int, head:int, limit:int):
        print(lista[head])
        element = lista[head]
        lista[head] = 0
        head = self._head_increment.head_increment(head,limit)
        return element
        
class Peek(_PeekInterface):
    def peek(self, lista:list, head:int):
        element = lista[head]
        print(f"Pierwszy element w kolejce to {element}")
        return element

class PrintContent(_PrintContentInterface):
    def print_content(self,lista:list, head:int, tail:int):
        print(lista)
        print(f"Head: {head} oraz tail: {tail}")

class ClearBuffer(_ClearBufferInterface):
    def clear_buffer(self,limit:int):
        lista = []
        for i in range(limit):
            lista.append(0)
        return lista
            
class ReplaceLast(_ReplaceLastInterface):
    def replace_last(self,tail,limit):
        if tail == 0:
            tail = limit-1
            return tail
        else:
            tail = tail - 1
            return tail

class IsFull(_IsFullInterface):
    def is_full(self,lista):
        licznik = 0
        for element in lista:
            if element == 0:
                licznik = licznik + 1
        if licznik==0:
            print("is_full")
            #print("true")
            return True
        else:
            #print("false")
            return False
            
class HeadIncrement(_HeadIncrementInterface):
    def head_increment(self,head,limit):
        print("head_increment")
        if head == limit-1:
            print("tutaj")
            return 0 
        else:
            print("Zwiększam")
            return head+1

class TailIncrement(_TailIncrementInterface):
    def tail_increment(self,tail,limit):
        print(f"tail_increment-{tail} ")
        if tail == limit-1:
            print("tutaj")
            return 0
        else:
            print("Zwiększam")
            print(f"wartosc {tail+1}")
            return tail+1



class Queue(_QueueInterface):
    def __init__(self,limit:int,is_empty:_IsEmptyInterface,
    size: _SizeInterface, enqueue: _EnqueueInterface, 
    dequeue:_DequeueInterface, peek: _PeekInterface, print_content: _PrintContentInterface, 
    clear_buffer: _ClearBufferInterface):
        self._lista=[]
        self._limit = limit
        self._tail = 0
        self._head = 0
        for i in range(self._limit): self._lista.append(0)
        self._is_empty = is_empty
        self._size = size
        self._enqueue = enqueue
        self._dequeue = dequeue
        self._peek = peek
        self._print_content = print_content
        self._clear_buffer = clear_buffer

    def size(self): self._size.size(self._lista,self._limit)

    def is_empty(self): self._is_empty.is_empty(self._lista)

    def peek(self): self._peek.peek(self._lista)

    def clear_buffer(self): self._clear_buffer.clear_buffer(self._limit)

    def print_content(self): self._print_content.print_content(self._lista,self._head,self._tail)

    def enqueue(self, x) : self._enqueue.enqueue(x,self,self._tail,self._limit)

    def dequeue(self) : self._dequeue.dequeue(self._lista,self._head,self._limit)


is_empty = IsEmpty()
size = Size()
is_full = IsFull()
replace = ReplaceLast()
tail_increment = TailIncrement()
enqueue = Enqueue(is_full,replace,tail_increment)
dequeue = Dequeue(head_increment=HeadIncrement())
peek = Peek()
print_content = PrintContent()
clear_buffer = ClearBuffer()
queue = Queue(10,is_empty,size,enqueue,dequeue,peek,print_content,clear_buffer)

queue.print_content()


