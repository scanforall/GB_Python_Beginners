#  -------------------------------------------------------- 1 ----------------------------------------------------------


a = "hello"
b = "world!"
print(f"{a}, {b}")
numb1 = int(input("Enter any number: "))
numb2 = int(input("Enter any number one more time: "))
print(f"You have chosen the numbers {numb1} and {numb2}")
word = input("Enter any word: ")
print(f"{word} - it's good choice")

#  -------------------------------------------------------- 2 ----------------------------------------------------------


time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


in_put = int(input("Введите время в секундах: "))

hours = in_put // 3600
seconds = in_put % 60
minutes = in_put % 3600 // 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

#  -------------------------------------------------------- 3 ----------------------------------------------------------


n = input("Enter an integer: ")

while n < '0':
    print("I've asked for number greater than 0! Please try again!")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

#  -------------------------------------------------------- 4 ----------------------------------------------------------


num_init = int(input("Введите целое положительное число: "))
greatest_dig = 0  # Переменная для хранения текущего максимума
num = num_init  # Переменная для хранения оставшейся части числа (см цикл)

while num > 0:  # Выполняем цикл, пока отсечения цифр числа (см ниже) его не обнулили
    digit = num % 10  # Определяем последнюю цифру
    if digit > greatest_dig:  # Сравниваем ее с текущим максимумом
        greatest_dig = digit  # При необходимости меняем текущий максимум
        if greatest_dig == 9:  # Это условие не обязательно, но экономит время исполнения. Цифр больше 9 не бывает.
            break
    num = num // 10  # Отсекаем от числа последнюю цифру

print(f"Наибольшая цифра в числе {num_init} равна {greatest_dig}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

# Функция с рекурсией

def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10


print(f"The largest number is: {num_max(int(input('Enter the number: ')))}")


#  -------------------------------------------------------- 5 ----------------------------------------------------------


revenue = float(input("Введите значение выручки (тугрики) - "))
costs = float(input("Введите значение издержек (тугрики) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result} тугриков!")
    print(f"Рентабельность выручки составила {100 * result / revenue:.1f}%")
    personal_n = int(input("Сколько счастливых целочисленных сотрудников работает в Вашей компании? "))
    print(f"Если Вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.3f} тугриков.")
elif result < 0:
    print(f"Увы, Ваша компания пока сработала с убытком {-result} тугриков! Старайтесь, у Вас все получится!")
else:
    print("Ноль - это тоже хороший результат! Попросите у друга тугрик и пропейте его вместе за стабильность!")

#  -------------------------------------------------------- 6 ----------------------------------------------------------


while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результаты должены быть больше нуля. Стартовое значение != 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьется результат за {days} дней")
        break


#  ------------------------------------------- вариант решения ---------------------------------------------------------

# Функция с рекурсией


def km(res_min, res_max, days):
    if res_min > res_max:
        return days
    else:
        return km(res_min * 1.1, res_max, days + 1)


print(km(int(input("Enter first param ")), int(input("Enter second param ")), 1))
