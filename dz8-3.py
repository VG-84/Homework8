# dz8-3

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Ввод значении'))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Введите число")
                y_or_n = input(f'Еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Выход'
                else:
                    return f'Выход'

try_except = Error(1)
print(try_except.my_input())