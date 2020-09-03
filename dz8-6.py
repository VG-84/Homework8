# dz8-4,5,6

class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} Цена {self.price} Количество {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Ввод названия')
            unit_p = int(input(f'Ввод цены'))
            unit_q = int(input(f'Ввод количества'))
            unique = {'Модель': unit, 'Цена': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список -\n {self.my_store}')
        except:
            return f'Ошибка'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь ассортимент -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print any {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan any {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier any {self.numb} times'


unit_1 = Printer('Cisco', 50000, 9, 15)
unit_2 = Scanner('Apple', 90000, 9, 14)
unit_3 = Copier('Pego Piper', 100000, 6, 5)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())