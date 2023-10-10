"""
Задание 3
Вам необходимо создать класс Airplane (самолет).
C помощью перегрузки операторов реализовать:
■ Проверка на равенство типов самолетов (операция ==);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможому количеству пассажиров на борту (операции > < <= >=).
"""
class Airplane:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

    def __eq__(self, other):
        return self.type == other.type

    def __add__(self, other):
        return self.quantity + other

    def __gt__(self, other):
        return self.quantity > other.quantity

    def __lt__(self, other):
        return self.quantity < other.quantity

    def __ge__(self, other):
        return self.quantity <= other.quantity

    def __le__(self, other):
        return self.quantity >= other.quantity

    def __add__(self, other):
        return self.quantity + other

    def __sub__(self, other):
        return self.quantity - other

    def __iadd__(self, other):
        self.quantity += other
        return self

    def __isub__(self, other):
        self.quantity -= other
        return self

    def __str__(self):
        return "Тип самолета {}, количество пасажиров {}".format(self.type, self.quantity)

a1 = Airplane("Ty-134", 180)
a2 = Airplane("Ty-154", 280)
print(a1)
print(a2)

#Проверка на равенство типов самолетов (операция ==);
print(a1 == a2)
#print("Изменили количество пассажиров a1:", a1 + 30)
#print("Вызывается магический метод __gt__", a1 > a2)

#Сравнение двух самолетов по максимально возможому количеству пассажиров на борту (операции > < <= >=)
print("Вызывается магический метод __gt__", a1 > a2) # Вызывается магический метод __gt__
print("Вызывается магический метод __lt__", a1 < a2) # Вызывается магический метод __lt__
print("Вызывается магический метод __ge__", a1 <= a2) # Вызывается магический метод __ge__
print("Вызывается магический метод __le__", a1 >= a2) # Вызывается магический метод __le__

#Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=)
print("Изменили количество пассажиров:", a1+30)
#print("Изменили количество пассажиров:", a1-15)

a1 += 30
print("Увеличили пассажиров на 30")
print(a1)

print("Уменьшили пассажиров на 50")
a1 -= 50
print(a1)