#  -------------------------------------------------------- 1 ----------------------------------------------------------

import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def __init__(self, light_list):
        self.light_list = light_list

    def running(self):
        if len([i for i in self.light_list if i in ["red", "yellow", "green"]]) >= 3:
            for light in itertools.cycle(self.__color):
                print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
                time.sleep(light[1][0])
        else:
            print("Your color list is incorrect.")


trafficlight_1 = TrafficLight(["lilac", "green", "lime", "white", "black", "yellow"])
trafficlight_1.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep
from itertools import cycle


class TrafficLight:
    #    __color = [[' RED ', 'YELLOW', 'GREEN'], [7, 2, 4],
    __color = ["   ", [7, 2, 4], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]

    def running(self):
        col_lst = ["", ""]
        for n in cycle((0, 1, 2)):
            col_lst[1] = self.__color[2][n]
            print(f"\r({col_lst[int(n == 0)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n == 1)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n == 2)]}{self.__color[0]}\033[0m)", end='')
            sleep(self.__color[1][n])


tr_light = TrafficLight()
tr_light.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from time import sleep
import colorama
import sys

colorama.init()


class TrafficLight:
    # Запуск в терминале
    def running(self):
        while True:
            print(f'\r\033[31m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[30m{chr(11035)} ')
            print(f'\r\033[33m{chr(11035)} ', end='')
            sleep(2)
            print(f'\r\033[30m{chr(11035)} ')
            print(f'\r\033[32m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[30m{chr(11035)} ', end='')
            sys.stdout.write('\r\x1b[2A')


trafficLight = TrafficLight()
trafficLight.running()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import tkinter as tk
from PIL import ImageTk, Image
from itertools import cycle


class TrafficLight:
    def __init__(self, working_algorithm):
        self.sec_count = 0
        self.working_algorithm = working_algorithm
        self.img_dict = {'red': Image.open('pic/tl_red.jpg').resize((350, 400)),
                         'yellow': Image.open('pic/tl_yellow.jpg').resize((350, 400)),
                         'green': Image.open('pic/tl_green.jpg').resize((350, 400)),
                         'red+yellow': Image.open('pic/tl_red_yellow.jpg').resize((350, 400)),
                         'off': Image.open('pic/tl_off.jpg').resize((350, 400))}
        self.iterator = cycle(self.working_algorithm)
        self.cur_state = next(self.iterator)

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.geometry('300x400')
        image = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
        self.label = tk.Label(image=image)
        self.label.pack(side="top", fill="both", expand="yes")
        self.running()
        self.root.mainloop()

    def running(self):
        self.sec_count += 1
        if self.sec_count == self.cur_state[1]:
            self.cur_state = next(self.iterator)
            self.sec_count = 0
            cur_img = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
            self.label.configure(image=cur_img)
            self.label.photo_ref = cur_img
            self.label.pack()
        self.root.after(100, self.running)


mode = input("Enter traffic-light mode (0 - simple, 1-advanced):")
if mode == '0':
    app = TrafficLight([('red', 70), ('yellow', 20), ('green', 50), ('yellow', 20)])
elif mode == '1':
    app = TrafficLight([('red', 70),
                        ('red+yellow', 20),
                        ('green', 50),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('yellow', 20)])
else:
    print('Wrong choice!')


#  -------------------------------------------------------- 2 ----------------------------------------------------------


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f" {(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Road:
    def __init__(self, le, wi):
        self._length = le
        self._width = wi

    def calc(self, weight=25, thickness=5):
        print(f"Масса асфальта - {self._length * self._width * weight * thickness / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width of road in m: ")), int(input("Enter lenght of road in m: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")


#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


meneger = Position("Dorian", "Grey", "СEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())


#  -------------------------------------------------------- 4 ----------------------------------------------------------

from random import choice


class Car:
    """ Main car """
    direction = ["🡡 north", "northeast 🡥", "east 🡢", "southeast 🡦",
                 "south 🡣", "🡧 southwest", "🡠 west", "🡤 northwest"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Сar stopped!')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):
    """ City car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """ Cargo truck """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ Sports Car """


class PoliceCar(Car):
    """ Patrol car """

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('"Полицайка"', 'белый', 80)
work_car = WorkCar('"Грузовичок"', 'хаки', 40)
sport_car = SportCar('"Спортивка"', 'красный', 120)
town_car = TownCar('"Малютка"', 'жёлтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

#  -------------------------------------------------------- 5 ----------------------------------------------------------


class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationery()
pen = Pen("Parker")
pencil = Pencil("Faber-Castell")
marker = Marker("COPIC")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()
