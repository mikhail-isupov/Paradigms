# Шаблон Singleton:
# Реализуйте паттерн Singleton на языке Python для класса Logger, 
# который будет использоваться для логирования информации в приложении. 
# Гарантируйте, что только один экземпляр класса Logger будет создан.

class Logger:
    _instance = None
    _log = []

    def __new__(self):
        if self._instance is None:
            self._instance = super(Logger, self).__new__(self)
        return self._instance
    
    def add(self, message):
        self._log.append(message)

    def view(self):
        for message in self._log:
            print(message)
    


print(Logger() is Logger())
Logger().add("Hello")
Logger().add("world!")
Logger().view()

