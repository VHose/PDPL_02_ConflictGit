class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def birthday(self):
        self.set_age(self.get_age() + 1)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def birthday(self):
        self.set_age(self.get_age() + 2)


s = Student("Iwan", 24)
print(f"{s.get_name()} {s.get_age()}")
s.birthday()
print(f"{s.get_name()} {s.get_age()}")
