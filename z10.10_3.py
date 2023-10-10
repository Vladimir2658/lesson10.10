"""
Задание 3
Вам необходимо создать класс Airplane (самолет).
C помощью перегрузки операторов реализовать:
■ Проверка на равенство типов самолетов (операция
= =);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможому количеству пассажиров на борту (операции >
< <= >=).
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

print(111)

a1 = Airplane("Ty-134", 180)
a2 = Airplane("Ty-154", 280)

print(a1 == a2)
print("Изменили количество пассажиров a1:", a1 + 30)
print("Вызывается магический метод __gt__", a1 > a2)
