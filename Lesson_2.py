#  -------------------------------------------------------- 1 ----------------------------------------------------------


my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
           (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10},
           frozenset(), range(11), b'twelve', bytearray(b'thirteen'),
           zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = list(input("Enter the numbers without space - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = input("Введите числа списка через пробел: ").split()
print('Введеный список: ', my_list)

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('Измененный список: ', my_list)


#  ------------------------------------------- вариант решения ---------------------------------------------------------


user_list = input("Enter the numbers with space - ").split()

for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))

print(user_list)


#  -------------------------------------------------------- 3 ----------------------------------------------------------


month = int(input("Введите интересующий вас месяц года от 1 до 12: "))

month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "декабрь"]


if month in month_dict:
    print(f"{month}-й месяц года - это {month_dict[month]}")
    print(f"{month}-й месяц года - это {month_list[month - 1]}")
else:
    print("Wrong number.")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month_num = int(input('Введи номер месяца(только цифра): '))

if month_num in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])


#  ------------------------------------------- вариант решения ---------------------------------------------------------


while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
        break
    else:
        print("Error!!!")

#  -------------------------------------------------------- 4 ----------------------------------------------------------


string = input("Enter the numbers with space - ").split()

for n, i in enumerate(string, 1):
    print(n, i) if len(i) <= 10 else print(n, i[:10])

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')

#  -------------------------------------------------------- 5 ----------------------------------------------------------


my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input("Введите новый элемент рейтинга в виде натурального числа: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

my_list = [7, 5, 3, 3, 2]

n = int(input('количество ввода: '))
for it in range(n):
    number = int(input('введите рейтинг: '))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, float(number))
    print(my_list)
    

#  -------------------------------------------------------- 6 ----------------------------------------------------------


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        f_copy[f] = int(pro) if f == 'цена' or f == 'количество' else pro  # Меняем тип числовых свойства
        analytics[f].append(f_copy[f])  # Добавляем свойство в аналитику
    goods.append((num, f_copy))  # Добавляем свойство в список товаров
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


i = 1
database = []
analytics = []
list_ = dict()

while True:
    start = input("Hi! I'm a database of goods. If you want to continue, enter 1. Finish - 0.\n -- ")
    if start == "0":
        l = []
        print("Do you want to do analytics?")
        answer = input("Yes - y, No - n ")
        while answer == "y":
            type_ = input("Enter analytics parameter: name, price, number, units - ")
            for j in range(len(database)):
                l.append(analytics[j].get(type_))
                list_[type_] = l
            answer = input("Do you want continue? Yes - y, No - n ")
        if answer == "n":
            if database:
                print(database)
            else:
                print("You have left the program")
        else:
            print("You mast enter 'y' or 'n'")
        print(database)
        print(list_)
        break
    elif start == "1":
        good_ = dict()
        good_["name"] = input("Enter name of good - ")
        good_["price"] = input("Enter price of good - ")
        good_["number"] = input("Enter number of good - ")
        good_["units"] = input("Enter units of good - ")
        database.append((i, good_))
        analytics.append(good_)
        i += 1
    else:
        print("You didn't enter the required numbers - 0 or 1.")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

enter = ''
goods = []
i = 0

while enter == '':  # если нажата клавиша Enter - вводим данные, иначе выходим
    i += 1

    name = input('\nEnter name of good: ')
    price = input('Enter price: ')
    num = input('Enter quantity of good: ')
    unit = input('Enter unit: ')

    goods.append((i, {'name': name, 'price': price, 'num': num, 'unit': unit}))
    print('\n', goods)

    enter = input('\nPress Enter for continue, any key+Enter to exit...')

# вывод "аналитики"
while True:
    print('\nChoose action: ')
    print(' [1] Print list of goods.')
    print(' [2] Print list of prices.')
    print(' [3] Print quantities.')
    print(' [4] Print units.')
    print(' [5] Exit.')

    action = input('\nYour choice: ')
    if action == '5':
        break

    names = ('Goods', 'Prices', 'Quantities', 'Units')
    titles = ('name', 'price', 'num', 'unit')
    res = {'name': [], 'price': [], 'num': [], 'unit': set()}

    for id, v in goods:
        res['name'].append(v['name'])
        res['price'].append(v['price'])
        res['num'].append(v['num'])
        res['unit'].add(v['unit'])

    print(res)

    print(f'\n{names[int(action) - 1]}: {res[titles[int(action) - 1]]}')

print('\nGoodbye!')
