
# 7-m
class Laptop:
    def __init__(self, brand, ram, storage, serial):
        self.brand = brand
        self._ram = ram
        self._storage = storage
        self.__serial = serial

    def upgrade_ram(self, x):
        self._ram += x

    def upgrade_storage(self, x):
        self._storage += x

    def info(self):
        print(f"RAM:{self._ram} Storage:{self._storage}")


l1 = Laptop("HP", 8, 256, "SN001")

l1.upgrade_ram(8)
l1.upgrade_storage(256)
l1.info()


# 8-m
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary
        self.hours = 0

    def teach(self, hours):
        self.hours = hours

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"Teaching {self.hours} hours")
        print(f"Salary:{self.__salary}")


t1 = Teacher("Ali", "Math", 1000)

t1.teach(2)
t1.increase_salary(200)
t1.info()
