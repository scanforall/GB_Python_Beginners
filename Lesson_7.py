#  -------------------------------------------------------- 1 ----------------------------------------------------------


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

# stroki = int(input("Введите количество строк и столбцов матрицы: "))
# stolbci = stroki
#
# matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
# matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])
#
# print('First matrix:\n', matrix1, end='\n\n')
# print('Second matrix:\n', matrix2, end='\n\n')
# print('Summ of first and second matrix:\n', matrix1 + matrix2)


#  ------------------------------------------- вариант решения ---------------------------------------------------------

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


m = [[1, 2, 3], [3, 4, 5], [1, 2]]
n = [[9, 8, 7], [7, 6, 5]]

matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print(matr_1 + matr_2)


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)

#  -------------------------------------------------------- 2 ----------------------------------------------------------


from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet


class Coat(Сlothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('На детей не шьем. Начнем с сорокового.')
            self.__size = 40
        elif size > 58:
            print('Не многовато ли? 58 - МАКСИМУМ, для него и посчитаем')
            self.__size = 58
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5


class Сostume(Сlothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('На детей не шьем.')
            self.__height = 150
        elif height > 240:
            print('Не многовато ли? 240 - МАКСИМУМ, для него и посчитаем')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Введите размер пальто для рассчета:')))
print(f'Вам потребуется {coat_1.raschet:.2f} метров ткани на пальто {coat_1.size} размера ')
costume_1 = Сostume(int(input('Введите рост для костюма для рассчета (как обычно, в сантиметрах):')))
print(f'Вам потребуется {costume_1.raschet:.2f} метров ткани на костюм {costume_1.height} роста ')
print(f'Всего вам потребуется {coat_1 + costume_1:.2f} метров ткани')


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, param=100):
        self.param = param

    @property
    def consumption_Coat(self, param):
        pass

    @property
    def consumption_Costume(self, param):
        pass

    @property
    def consumption(self):
        return self.consumption_Coat + self.consumption_Costume


class Coat(Clothes):
    @property
    def consumption(self):
        result = round(self.param / 6.5 + 0.5, 2)
        Clothes.consumption_Coat = result
        return f'Расход ткани для пальто - {self.param} размера = {round(self.param / 6.5 + 0.5, 2)}'


class Costume(Clothes):
    @property
    def consumption(self):
        result = round(2 * self.param + 0.3, 2)
        Clothes.consumption_Costume = result
        return f'Расход ткани для костюм - на рост {self.param} = {round(2 * self.param + 0.3, 2)}'


my_1 = Clothes()
my_2 = Coat(35)
print(my_2.consumption)
my_3 = Costume(183)
print(my_3.consumption)
print(f'Общий расход ткани = {my_1.consumption}')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Cell:
    def __init__(self, nums):
        self.nums = nums  # 13

    def make_order(self, rows):  # 5
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Sum of cell is:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Subtraction of cell is:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Multiply of cell is:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Truediv of cell is:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
