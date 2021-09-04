#  -------------------------------------------------------- 1 ----------------------------------------------------------


from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

from random import randint


original_list = [randint(0, 1000) for _ in range(0, randint(2, 20))]
answer_list = [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

print(original_list)
print(answer_list)

#  -------------------------------------------------------- 3 ----------------------------------------------------------


uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

#  -------------------------------------------------------- 4 ----------------------------------------------------------


from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


print(a := [randint(0, 9) for _ in range(20)], [i for i in a if a.count(i) == 1], sep="\n")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

#  -------------------------------------------------------- 6 ----------------------------------------------------------


from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print(
    'Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода'
    ' из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("ABC")

for _ in range(5):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        #  repeat_list = [el for el in islice(cycle(my_list), num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"


print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import count, cycle

# а)
iterator = count(int(input('Введите целое число, начиная с которого будут генерироваться числа: ')))
print('Первые десять чисел начиная с введенного вами числа:')
for i in range(10):
    print(next(iterator), end=' ')

# б)
print('\n- cycle -')
lst = ['string', 101, 3.1415, 15.457]
iterator = cycle(lst)
# Перебираем элементы списка два раза.
for i in range(len(lst) * 2):
    print(next(iterator), end=' ')


#  -------------------------------------------------------- 7 ----------------------------------------------------------

from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)



x = 0
for i in fact_gen():
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


def fact_gen(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1


for el in fact_gen(int(input('Factorial number: '))):
    print(el)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from functools import reduce


def fact(n):
    try:
        yield reduce(lambda x, y: x * y, list(el if el > 0 else 1 for el in range(n + 1)))
    except TypeError:
        yield 0


for i in fact(0):
    print(i)

