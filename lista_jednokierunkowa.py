from abc import ABC, abstractmethod

class ListInterface(ABC):
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

class OneWayList(ListInterface):
    
    def is_empty(self):  pass
    
    def size(self):  pass
    
    def insert(self, x, a):  pass
    
    def remove(self,x):  pass
    
    def remove_at(self,a):  pass
    
    def find_all(self,condition):  pass
