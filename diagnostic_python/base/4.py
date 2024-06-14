import copy
class House:
    def __init__(self, name, place, size=100):
        self.name = name
        self.place = place
        self.size = size
    def __str__(self):
        # по умолчанию функция print() использует специальные методы класса __str__() или __repr__() для формирования строкового представления объекта. 
        # если эти методы не определены в классе, то Python использует дефолтное представление, которое включает в себя имя класса и адрес в памяти, где хранится объект.
        return f"{self.name}'s House, {self.place} ({self.size})"
    def change_owner(self, new_owner):
        self.name = new_owner
    def __call__(self):
        hs = len(self.place)*self.size
        return hs
    def __iadd__(self, value):
        self.size += value
        return self
    def __floordiv__(self, other):
        result = copy.deepcopy(self)
        result.name = f'{self.name} {other.name}'
        result.place = other.place
        result.size = (self.size + other.size) // 2
        return result
    def __gt__(self, other): # >
        if self.size == other.size:
            if len(self.place) == len(other.place):
                if self.name == other.name:
                    return False
                else:
                    return self.name > other.name
            else:
                return len(self.place) > len(other.place)
        else:
            return self.size > other.size
    def __ge__(self, other): # >=
        if self.size == other.size:
            if len(self.place) == len(other.place):
                if self.name == other.name:
                    return True
                else:
                    return self.name >= other.name
            else:
                return len(self.place) >= len(other.place)
        else:
            return self.size >= other.size
    def __lt__(self, other): # <
        if self.size == other.size:
            if len(self.place) == len(other.place):
                if self.name == other.name:
                    return False
                else:
                    return self.name < other.name
            else:
                return len(self.place) < len(other.place)
        else:
            return self.size < other.size
    def __le__(self, other): # <=
        if self.size == other.size:
            if len(self.place) == len(other.place):
                if self.name == other.name:
                    return True
                else:
                    return self.name <= other.name
            else:
                return len(self.place) <= len(other.place)
        else:
            return self.size <= other.size
hs = House('Marran', 'Salt Beach')
print(hs, hs(), sep='\n')
id_hs = id(hs)
hs += -20
hs.change_owner('Rual')
print(hs)
print(id_hs == id(hs))
print()
hs = House('Lart', 'Mount', 57)
hs1 = House('Sam', 'Fast River')
print(hs, hs1, sep='\n')
print(hs > hs1, hs <= hs1, hs == hs1)
hs2 = hs // hs1
print(hs2)
print(hs2 < hs1, hs2 >= hs, hs2 != hs1)
