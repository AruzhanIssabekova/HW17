# class Car:
#     def __init__(self):
#         self.model = ""
#         self.year = 0
#         self.proiz = ""
#         self.obom = 0
#         self.color = ""
#         self.price = 0
#     def input_data(self):
#         self.model = input("Введите название модели: ")
#         self.year = int(input("Введите год выпуска: "))
#         self.proiz = input("Введите производителя: ")
#         self.obom = int(input("Введите объем двигателя: "))
#         self.color = input("Введите цвет машины: ")
#         self.price = int(input("Введите цену: "))
#     def output_data(self):
#         print(f"\nИнформация об автомобиле:")
#         print(f"Модель: {self.model}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Производитель: {self.proiz}")
#         print(f"Объем двигателя: {self.obom} л")
#         print(f"Цвет машины: {self.color}")
#         print(f"Цена: {self.price}")
#
#         def model(self):
#             return self.model
#
#         def year(self):
#             return self.year
#
#         def proiz(self):
#             return self.proiz
#
#         def obom(self):
#             return self.obom
#
#         def color(self):
#             return self.color
#
#         def price(self):
#             return self.price
# car1 = Car()
# car1.input_data()
# car1.output_data()
# print(car1.price)




# class Book:
#     def __init__(self):
#         self.name = ""
#         self.year = 0
#         self.izd = ""
#         self.zhanr = 0
#         self.avtor = ""
#         self.price = 0
#     def input_data(self):
#         self.name = input("Введите название книги: ")
#         self.year = int(input("Введите год выпуска: "))
#         self.izd = input("Введите издателя: ")
#         self.zhanr = input("Введите жанр книги: ")
#         self.avtor = input("Введите автора книги: ")
#         self.price = int(input("Введите цену: "))
#     def output_data(self):
#         print(f"\nИнформация о книге:")
#         print(f"название: {self.name}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Издатель: {self.izd}")
#         print(f"Жанр: {self.zhanr}")
#         print(f"Автор: {self.avtor}")
#         print(f"Цена: {self.price}")
#
#         def name(self):
#             return self.name
#
#         def year(self):
#             return self.year
#
#         def izd(self):
#             return self.izd
#
#         def zhanr(self):
#             return self.zhanr
#
#         def avtor(self):
#             return self.avtor
#
#         def price(self):
#             return self.price
# book1 = Book()
# book1.input_data()
# book1.output_data()
# print(book1.zhanr)





# class Stadion:
#     def __init__(self):
#         self.name = ""
#         self.year = 0
#         self.country = ""
#         self.city = 0
#         self.vmest = ""
#     def input_data(self):
#         self.name = input("Введите название стадиона: ")
#         self.year = int(input("Введите год открытия: "))
#         self.country = input("Введите страну: ")
#         self.city = input("Введите город: ")
#         self.vmest = int(input("Введите вместимость: "))
#     def output_data(self):
#         print(f"\nИнформация о стадионе:")
#         print(f"Название: {self.name}")
#         print(f"Год открытия: {self.year}")
#         print(f"Страна: {self.country}")
#         print(f"Город: {self.city}")
#         print(f"Вместимость: {self.vmest}")
#
#         def name(self):
#             return self.name
#
#         def year(self):
#             return self.year
#
#         def izd(self):
#             return self.country
#
#         def zhanr(self):
#             return self.city
#
#         def vmest(self):
#             return self.vmest
#
# stadion1 = Stadion()
# stadion1.input_data()
# stadion1.output_data()
# print(stadion1.city)




class Main:
    def __init__(self, text=''):
        self.text = text

    def new_text(self, text_new=''):
        self.text = text_new
class Sub(Main):
    def __init__(self, text='', numeric=0):
        super().__init__(text)
        self.numeric = numeric

b = Main('Текст')
print(b.text)
b.new_text("Новое значение текста")
print(b.text)
c = Sub("Текст потомка", 42)
print(c.text)
print(c.numeric)
c.new_text("Новый текст потомка")
print(c.text)

