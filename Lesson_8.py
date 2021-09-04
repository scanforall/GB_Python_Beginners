#  -------------------------------------------------------- 1 ----------------------------------------------------------


"""
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу
«Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Number(int):
    def __str__(self):
        return f"{self:02}"

class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        day, month, year = self.transform(date.split('-'))

        if not self.validate(day, month, year):
            raise ValueError(f"{date} inalid date format")

        self.day = day
        self.month = month
        self.year = year

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date):
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date):
        if not all(map(lambda x: isinstance(x, int), date)):
            return False

        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'.'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    try:
        print(Date('31-12-2022'))
        print(Date('41-01-1970'))
    except ValueError as e:
        print(e)


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        is_date = cls.is_date_valid(date_as_string)
        try:
            if is_date == False:
                raise OwnError("Wrong date!")
        except OwnError as err:
            print(err)
            return

        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-10-2012')

try:
    print(date2.day, date2.month, date2.year)
except:
    print('OOps. Something wrong')


#  ------------------------------------------- вариант решения ---------------------------------------------------------

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_type(cls, data):
        return f'День {int(data[0]):02d}, Месяц {int(data[1]):02d}, Год {int(data[2])}'

    @staticmethod
    def validation(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'Введена некоррекная дата!'

    def data_func(self):
        result_1 = Data.change_type(self.data.split('-'))
        result_2 = Data.validation(self.data.split('-'))
        return result_2 if result_2 else f'Переформатированная дата (тип int)\n{result_1}'


user_data = input('Введите дату (чч-мм-гг): ')
mc = Data(user_data)
print(mc.data_func())
user_data = input('Введите дату (чч-мм-гг): ')
mc_2 = Data(user_data)
print(mc_2.data_func())
print(mc.data_func())


#  -------------------------------------------------------- 2 ----------------------------------------------------------

class MyZeDiEr(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            raise MyZeDiEr("Division by zero forbidden!!!")
        return round(s_1 / s_2, 3)
    except ValueError:
        return "Value Error"
    except MyZeDiEr as my:
        return my


print(div(input("Enter first number - "), input("Enter first second - ")))


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class MyDivisionZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


div = lambda x, y: x / y if y != 0 else MyDivisionZeroError('Ошибка дедения на 0!!')

print(div(1, 0))

print(div(4, 2))


#  -------------------------------------------------------- 3 ----------------------------------------------------------


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    inp_data = input("Введите число: ")
    if inp_data == "":
        break
    try:
        if inp_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(inp_data))
        else:
            raise OwnError("введено не число")
    except OwnError as err:
        print(err)
        continue

print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import re


class NotNumeric(Exception):
    def __init__(self, text):
        self.text = text


num = re.compile(r'^[-+]?\d+[,.]?\d*$')
result = []

while True:
    try:
        el = input('Введите элемент списка(число): ')
        if el.lower() == 'stop':
            break
        elif num.match(el):
            result.append(el)
        else:
            raise NotNumeric('Число число')
    except NotNumeric as err:
        print(err)
print(result)


#  ------------------------------------------- вариант решения ---------------------------------------------------------

class MyList:
    print_list = []

    # Попробуем сделать исключение как класс в классе..
    @staticmethod
    class NotFloatExcept(Exception):
        def __init__(self, txt):
            self.txt = txt

    # Проверим что вновь введенная строка является числом, если да, перобразуем к числовому типу
    def __is_float(self, input_str):
        is_one_dot, is_one_minus = 0, 0
        for i in input_str:
            if ord(i) >= 48 and ord(i) <= 57:
                pass
            # В числе может быть одн точка
            elif ord(i) == 46 and is_one_dot == 0:
                is_one_dot += 1
            # А еще минус
            elif ord(i) == 45 and is_one_minus == 0:
                is_one_minus += 1
            else:
                raise self.NotFloatExcept('Введенная строка не является числом!')

        #  Если число целое, так и вернем
        if is_one_minus == 1 and len(input_str) == 2:
            return int(input_str)
        elif is_one_minus == 1:
            raise self.NotFloatExcept('Введенная строка не является числом!')
        elif is_one_dot == 0:
            return int(input_str)
        return float(input_str)

    # Добавляем новое число в список
    def __call__(self, new_str):
        try:
            self.print_list.append(self.__is_float(new_str))
        except self.NotFloatExcept as e:
            print(e)

    # Выводим на печать
    def __str__(self):

        return str(self.print_list)[1:-1]


list = MyList()

while True:
    print('Введите число: ', end='')
    n = input()
    if n == '':
        print('Окончание программы')
        break
    else:
        list(n)
        print(list)


#  -------------------------------------------------------- 4 ----------------------------------------------------------


class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    ''' Принтер '''

    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Сканер '''


class Copier(OfficeEquipment):
    ''' Копир '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    ''' Склад '''
    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):
        ''' Приём оргтехники на склад '''
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        ''' Выдача оргтехники со склада '''
        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nЗапасы на складе:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')
        print('------------------------------------')

    def issued_equipments(self):
        ''' Вывод информации овыданной оргтехикие '''
        print(f'\nIssued to office:\n{self.__equipments}')


# список моделей оргтехники
models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet'),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet'),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    # меню операций
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:  # если выбрана операция
        # формируем список оргтехники
        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} шт.)'
        # меню оргтехники
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            # выбираем модель
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
                    # вводим кол-во
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nОперация:')
                if (action == '1'):  # принимаем технику на склад
                    print(f'Принято на склад {models[model].model} - {n} шт.')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):  # выдаём технику со склада
                    max = warehouse.num(model)
                    if (n > max):  # если запрошено больше, чем есть
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    warehouse.issue_Equipment(model, n)

                # выводим остатки по складу
                warehouse.equipments_in_warehouse()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import datetime
from abc import ABC, abstractmethod
from view import Show_dict_cards, Show_dict_storage_points, Show_balans_storage_point


class Essence:
    def __init__(self, name):
        self._name = name
        self._id = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Dict_entities(dict):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._id_counter = 0

    def add(self, essence):
        essence.set_id(self._id_counter)
        self[self._id_counter] = essence
        self._id_counter += 1
        return essence.get_id()

    def get_name(self):
        return self._name


class Dict_cards(Dict_entities):
    def __init__(self):
        super().__init__('Список карточек ТМЦ')


class Card_item(Essence):
    def __init__(self, name, description='', price=0.0):
        super().__init__(name)
        # description - описание ТМЦ
        # price - цена за единицу
        self._description = description
        self._price = price

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price


class Dict_storage_points(Dict_entities):
    # Словарь точек хранения
    def __init__(self):
        super().__init__('Список точек хранения и контрагентов.')


class Dict_move_item(Dict_entities):
    # Словарь записей в амбарную книгу
    def __init__(self, name):
        super().__init__(name)


class Record_move_item(Essence):
    # Запись в амбарную книгу о перемещении ТМЦ
    def __init__(self, dttm, st_pnt, move_st_pnt, card, quantity):
        super().__init__('')
        # _dttm - дата и время двиения ТМЦ
        # _st_pnt -  точка хранения
        # _move_st_pnt - корреспондирующая точка хранения. Если приход то откуда, если расход то куда
        # _произоло перемещение ТМЦ
        # _card - карточки ТМЦ
        # _quantity - количество перемещаемых едениц ТМЦ если положительное то приход, если отрицательное то расход
        self._dttm = dttm
        self._st_pnt = st_pnt
        self._move_st_pnt = move_st_pnt
        self._card = card
        self._quantity = quantity

    def get_dttm(self):
        return self._dttm

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Movable_item:
    def __init__(self, st_pnt, card, quantity):
        self._st_pnt = st_pnt
        self._card = card
        self._quantity = quantity

    def get_st_pnt(self):
        return self._st_pnt

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Storage_point(Essence):
    def __init__(self, name, description, provider, dict_move_item, dict_cards):
        super().__init__(name)
        self._description = description
        self._provider = provider  # True - организация поставщик, False - точка хранения
        self._dict_move_item = dict_move_item
        self._dict_cards = dict_cards
        self._list_id_move_items = []

    def get_description(self):
        return self._description

    def get_provider(self):
        return self._provider

    def income(self, movable_item):
        record_move_item = Record_move_item(datetime.datetime.now(), self, movable_item.get_st_pnt(),
                                            movable_item.get_card(), movable_item.get_quantity())

        self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
        # self._dict_move_items.add
        #
        #
        #
        pass

    def flow(self, new_st_pnt, card, quantity):
        if self.calc_balance(card) >= quantity:
            record_move_item = Record_move_item(datetime.datetime.now(), self, new_st_pnt, card, -quantity)

            #      добавляю запись о расходе
            self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
            #      формирую movable_item
            movable_item = Movable_item(self, card, quantity)

            #      Передаю Inventory_item на новую точку хранения
            new_st_pnt.income(movable_item)
        # else:
        #     # возвращаю отказ в перемещении
        #     pass
        pass

    def calc_balance(self, card):
        # расчитывается остаток ТМЦ карточке
        balance = 0
        for i in self._list_id_move_items:
            if self._dict_move_item[i].get_card() is card:
                balance += self._dict_move_item[i].get_quantity()
        return balance

    def get_list_cards(self):
        # Возвращает список карточек ТМЦ, по которым было дижение на данной точке хранения
        list_id_cards = []
        list_card = []
        for i in self._list_id_move_items:
            list_id_cards.append(self._dict_move_item[i].get_card().get_id())
        for i in frozenset(list_id_cards):
            list_card.append(self._dict_cards[i])
        return list_card


def main():
    dict_move_item = Dict_move_item('')

    dict_cards = Dict_cards()
    dict_cards.add(Card_item('Компьютер', 'DeskTop', 25000.0))
    dict_cards.add(Card_item('Компьютер', 'Notebook', 35000.0))
    dict_cards.add(Card_item('Принтер', 'HP Laser Jet 1018', 6000.0))
    dict_cards.add(Card_item('Картридж', 'HP Q2612L экономичный 12L', 780.0))

    print()
    Show_dict_cards(dict_cards)()

    dict_storage_points = Dict_storage_points()
    dict_storage_points.add(Storage_point('Поставщик', 'Oldi', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Поставщик', 'ФЦентр', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Склад', 'Г-образная комната', False, dict_move_item, dict_cards))
    dict_storage_points.add(
        Storage_point('Склад', 'Помещение кроссового оборудования', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Цех №3', 'ТМЦ переданные в производство', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Списание', 'ТМЦ списанные ', False, dict_move_item, dict_cards))
    dict_storage_points.add(
        Storage_point('Утилизация', 'ООО \"Инвестиции в будущее\"', True, dict_move_item, dict_cards))

    print()
    Show_dict_storage_points(dict_storage_points)()

    Show_balans_storage_point(dict_storage_points[0])()
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    Show_balans_storage_point(dict_storage_points[0])()

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 6))
    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 12))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))

    dict_storage_points[1].flow(dict_storage_points[2], dict_cards[3], 12)
    dict_storage_points[0].flow(dict_storage_points[3], dict_cards[0], 3)

    print()
    Show_balans_storage_point(dict_storage_points[0])()
    Show_balans_storage_point(dict_storage_points[1])()
    Show_balans_storage_point(dict_storage_points[2])()
    Show_balans_storage_point(dict_storage_points[3])()
    Show_balans_storage_point(dict_storage_points[4])()


if __name__ == '__main__':
    main()

#  -------------------------------------------------------- модуль view ------------------------------------------------

import datetime


class Show_dict_cards:
    def __init__(self, dict_cards):
        self._dict_cards = dict_cards

    def __call__(self):
        print(f'  {self._dict_cards.get_name()}')
        print('+--------------+-----------------+---------------------------------------------+--------------+')
        print('|           id | Категория ТМЦ   | Описание                                    |  Цена за ед. |')
        print('+--------------+-----------------+---------------------------------------------+--------------+')
        for key, card_item in self._dict_cards.items():
            print(
                f'| {card_item.get_id():12} | {card_item.get_name():15} | {card_item.get_description():43} | {card_item.get_price():12.2f} |')
        print('+--------------+-----------------+---------------------------------------------+--------------+')


class Show_dict_storage_points:
    def __init__(self, dict_storage_points):
        self._dict_storage_points = dict_storage_points

    def __call__(self):
        print(f'  {self._dict_storage_points.get_name()}')
        print('+--------------+-----------------+---------------------------------------+-----+')
        print('|           id | Наименование    | Описаниея                             |Контр|')
        print('+--------------+-----------------+---------------------------------------+-----+')

        for key, storage_point in self._dict_storage_points.items():
            sprovider = 'Да' if storage_point.get_provider() else 'Нет'
            print(
                f'| {storage_point.get_id():12} | {storage_point.get_name():15} | {storage_point.get_description():37} | {sprovider:3} |')

        print('+--------------+-----------------+---------------------------------------+-----+')


class Show_balans_storage_point:
    def __init__(self, storage_point):
        self._storage_point = storage_point

    def __call__(self):
        print()
        print(
            f'Остатки на точке хранения: {self._storage_point.get_name()} ({self._storage_point.get_description()}) (id = {self._storage_point.get_id()})')
        print(f'по состоянию на {datetime.datetime.now()}')
        if len(self._storage_point.get_list_cards()) > 0:
            _total = 0.0
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')
            print(
                '|           id | Категория ТМЦ   | Описание                                    |  Цена за ед. |     Остаток |        Сумма |')
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')

            for i in self._storage_point.get_list_cards():
                _sum = i.get_price() * self._storage_point.calc_balance(i)
                _total += _sum
                print(
                    f'| {i.get_id():12} | {i.get_name():15} | {i.get_description():43} | {i.get_price():12.2f} |{self._storage_point.calc_balance(i):12} | {_sum:12.2f} |')
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')
            print(
                f'                                                                                                      Итого:  {_total:12.2f} ')
        else:
            print('Остатки не выявлены')


#  -------------------------------------------------------- 7 ----------------------------------------------------------


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))


cn = ComplexNumber(1, -2)
cn1 = ComplexNumber(3, 4)
print(cn + cn1)
print(cn * cn1)
print(complex(1, -2) * complex(3, 4))  # calculation check
