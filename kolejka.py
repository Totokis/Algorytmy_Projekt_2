class Stack(object):
#
    def __init__(self,limit):
        super().__init__()
        self._lista=[]
        self._limit = limit
        for i in range(self._limit):
            self._lista.append(0)
        self._head = 0
        self._tail = 0

    def wypisz(self):
        print(self._lista)
        print(f"Head: {self._head} oraz tail: {self._tail}")

    def wyczysc(self):
        for i in range(self._limit):
            self._lista.append(0)
            
    def _isFull(self):
        licznik = 0
        for element in self._lista:
            if element == 0:
                licznik = licznik + 1
            
        if licznik==0:
            #print("true")
            return True
        else:
            #print("false")
            return False


    def _tailIncrement(self):
        if self._tail == self._limit-1:
            self._tail = 0
        else:
            self._tail+=1

    def _headIncrement(self):
        if self._head == self._limit-1:
            print("tutaj")
            self._head = 0
        else:
            print("Zwiększam")
            self._head+=1
        
#
    def zakolejkuj(self, *elements):
        for element in elements:
            if self._isFull():
                print(f"Limit kolejki został osiągnięty, zostanie usunięty ostatni element :({self._lista[self._tail]}) i dodany ten najnowszy :({element})")
                #self._lista.pop()
                self._lista[self._tail] = element
                self._tailIncrement()
            else:
                self._lista[self._tail] = element
                self._tailIncrement()
#
    def odkolejkuj(self):
        #wersja nie jako bufor cykliczny  return self.lista.pop(0)
        print(self._lista[self._head])
        element = self._lista[self._head]
        self._lista[self._head] = 0
        self._headIncrement()
        return element
#



