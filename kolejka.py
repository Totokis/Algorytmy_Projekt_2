class _ReplaceLast:
    def replace_last(self,tail,limit):
        if tail == 0:
            tail = limit-1
            return tail
        else:
            tail = tail - 1
            return tail

class _IsFull():
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
            
class _HeadIncrement():
    def head_increment(self,head,limit):
        print("head_increment")
        if head == limit-1:
            print("tutaj")
            return 0 
        else:
            print("Zwiększam")
            return head+1

class _TailIncrement:
    def tail_increment(self,tail,limit):
        print(f"tail_increment-{tail} ")
        if tail == limit-1:
            print("tutaj")
            return 0
        else:
            print("Zwiększam")
            print(f"wartosc {tail+1}")
            return tail+1
        

class Stack():
    def __init__(self,limit):
        self._lista=[]
        self._limit = limit
        #*Zapełnienie listy#TODO zmienić na NULL
        for i in range(self._limit):
            self._lista.append(0)
        self._head = 0
        self._tail = 0
        self._is_full = _IsFull()
        self._tail_increment = _TailIncrement()
        self._head_increment = _HeadIncrement()
        self._replace_last = _ReplaceLast()

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
#
    def enqueue(self, *elements):
        for element in elements:
            if self._is_full.is_full(self._lista):
                self._tail = self._replace_last.replace_last(self._tail,self._limit)
                print(f"Limit kolejki został osiągnięty, zostanie usunięty ostatni element :({self._lista[self._tail]}) i dodany ten najnowszy :({element})")
                #self._lista.pop()
                self._lista[self._tail] = element
                self._tail = self._tail_increment.tail_increment(self._tail, self._limit)

            else:
                print("Jaki"+str(self._tail))
                self._lista[self._tail] = element
                self._tail = self._tail_increment.tail_increment(self._tail, self._limit)
                print(self._tail)
#
    def dequeue(self):
        print(self._lista[self._head])
        element = self._lista[self._head]
        self._lista[self._head] = 0
        self._head = self._head_increment.head_increment(self._head,self._limit)
        return element

    def peek(self):
        element = self._lista[self._head]
        print(f"Pierwszy element w kolejce to {element}")
        return element
#

#testowanie




# stack.enqueue("czwarty")
# stack.print_content()
# stack.dequeue()
# stack.print_content()


