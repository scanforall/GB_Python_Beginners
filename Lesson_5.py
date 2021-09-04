#  -------------------------------------------------------- 1 ----------------------------------------------------------


with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        # f.write(f"{line}\n")
        print(line, file=f)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


print('Введите данные для записи в файл \nДля окончания ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f"{line}\n")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_file = open("text_1.txt", 'w', encoding='utf-8')

line = " "
while line:
    line = input("пишите или не пишите!: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()

#  -------------------------------------------------------- 2 ----------------------------------------------------------


with open("text_2.txt", "r", encoding='utf-8') as f_obj:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
                  for line, count in enumerate(f_obj, 1)]
    print(*usefulness, f"Всего строк - {len(usefulness)}.", sep="\n")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open("text_2.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f'Строка {index} содержит {number_of_words} слов')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


with open('text_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')


task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')

#  -------------------------------------------------------- 4 ----------------------------------------------------------


rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding='utf-8') as new_file:
    with open("text_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])


#  ------------------------------------------- вариант решения ---------------------------------------------------------
# pip install googletrans==3.1.0a0
# обновление до альфа-версии

from googletrans import Translator

with open("text_4_translate.txt", 'w', encoding='utf-8') as f:
    with open("text_4.txt", 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print("DDoS-атака на Google не прошла, продолжаем попытки!")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


import requests
import json

"""Переводит с английского на русский файл, результат записывается в новый файл.
Должен быть установлен модуль requests.
"""
token = "trnsl.1.1.20200416T132512Z.0bdb58c00f70557b.b1aec4ed1dc72e76cc6c08980f7ed0c2de92ae86"
url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

with open("task_4_text_yandex.txt", "w", encoding="utf-8") as f_result:
    with open("text_4.txt", encoding="utf-8") as f_4:
        for line in f_4:
            eng_text = line
            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params=trans_option)
            trans_dict = json.loads(webRequest.text)
            line_to_result = "".join(trans_dict["text"])
            f_result.write(line_to_result)

print(f"Text translate from {f_4.name} has been done in {f_result.name}")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from random import randint

with open("text.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from random import randint


with open('task_5_file.txt',  mode='w+', encoding='utf-8') as the_file:
    the_file.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))


#  -------------------------------------------------------- 6 ----------------------------------------------------------


mydict = {}
with open("text_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        mydict[name] = name_sum
print(f"{mydict}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', 'r', encoding='utf8') as text_file:
    a = text_file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


dic = {}
numbers = "1234567890 "

with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        head, hours = line.split(":")
        dic[head] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dic)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '') \
            .replace('(пр)', '').replace('(лаб)', '').split()
        subj[line[0]] = sum(map(int, line[1:]))
    print(f'Общее количество часов по предмету: \n{subj}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


result = {}
with open("text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_timing = []
        lessons = ([el for el in line.split(" ")])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', 'r', encoding='utf-8') as file:
    print({string.split(':')[0]: sum([int(s[:s.index('(')]) for s in string.split() if '(' in s]) for string in file})


#  ------------------------------------------- вариант решения ---------------------------------------------------------

import re

subs_total_hours = {}

with open("text_6.txt") as f:
    for line in f.readlines():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(subs_total_hours)

#  -------------------------------------------------------- 7 ----------------------------------------------------------


import json

with open("my_ex7.json", "w", encoding="utf-8") as write_f:
    with open("text_7.txt", encoding="utf-8") as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from json import dump

with open('text_7.txt', 'r', encoding='utf-8') as read_file:
    with open('text_77.json', 'w', encoding='utf-8') as write_file:
        dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in read_file}
        average_profit_lst = []
        for n in dictionary.values():
            if n > 0:
                average_profit_lst.append(n)
        dump([dictionary, {"average_profit": sum(average_profit_lst) / len(average_profit_lst)}],
             write_file, ensure_ascii=False, indent=4)
