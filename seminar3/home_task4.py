# Шаблон Наблюдатель:
# Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. 
# Создайте класс NotificationSystem (наблюдаемый объект), 
# который будет иметь методы для добавления наблюдателей и уведомления о событиях. 
# Создайте несколько наблюдателей, реагирующих на уведомления.

class Observer:
    def __init__(self, observer_name):
        self.observer_name = observer_name

    def react(self, object):
        print(f"Наблюдатель {self.observer_name} увидел что с {object} что то произошло")

class NotificationSystem:
    _observers = []

    def __init__(self, object_name):
        self.object_name = object_name
    
    def __str__(self):
        return self.object_name

    def attach(self, observer):
        NotificationSystem._observers.append(observer)

    def alert(self):
        for observer in self._observers:
            observer.react(self)

observable1 = NotificationSystem("Объект 1")
observable2 = NotificationSystem("Объект 2")
observable1.attach(Observer("Номер 1"))
observable1.attach(Observer("Номер 2"))
observable1.alert()
observable2.alert()
