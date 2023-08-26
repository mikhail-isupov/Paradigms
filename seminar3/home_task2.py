# ООП Концепции:
# Создайте класс Person, который имеет атрибуты name, age и метод introduce(), 
# выводящий информацию о человеке. 
# Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.
class Person:
    def __init__(self, name = "NoName", age = 0):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

persons = [Person("Боб", 40), Person("Майк", 44), Person("Лиз", 33)]

for person in persons:
    person.introduce()