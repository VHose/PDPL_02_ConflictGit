import math
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

    def __str__(self):
        return f"{self.hitung_luas()}"

def print_bentuk(b: Bentuk):
    print(b)

class Persegi(Bentuk):
    def __init__(self, sisi=1):
        self.set_sisi(sisi)

    def get_sisi(self):
        return self.__sisi
    
    def set_sisi(self, value):
        self.__sisi = math.fabs(value)

    def hitung_luas(self):
        s = self.get_sisi()
        return s * s
    

class Lingkaran(Bentuk):
    def __init__(self, radius=1):
        self.set_radius(radius)

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        self.__radius = math.fabs(value)

    def hitung_luas(self):
        r = self.get_radius()
        return math.pi * r ** 2    

    
p = Persegi(2)
print(p)
print_bentuk(p)

l = Lingkaran(7)
print_bentuk(l)