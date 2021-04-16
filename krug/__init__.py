import math
from time import sleep

x0 = 5
y0 = 10
x1 = 8
y1 = 7

class Circle:
    def __init__(self, x0, y0, x1, y1, R, r, _x0=None, _y0=None, _x1=None, _y1=None, _R=None, _r=None):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.R = R
        if self.x0 > 0 and self.y0 > 0 and self.x1 > 0 and self.y1 > 0 and self._x0 is None and self._y0 is None and self._x1 is None and self._y1 is None and self._R is None and self._r is None:
            if self.R > 0 and self.r > 0:
                width = self.R - self.r
                if width >= 1:
                    aver1 = (self.x0 + self.x1)
                    aver2 = (self.y0 + self.y1)
                    d1 = abs(self.x0 - self.x1)
                    d2 = abs(self.y0 - self.y1)
                    if d1 == d2 and d1 >= 4 and d2 >= 4:
                        xo = aver1 / 2
                        yo = aver2 / 2
                        print("Координаты круга: (", xo, "; ", yo, ")")
                        half_D = d1 / 2
                        if self.R <= half_D and self.r >= 1:
                            print("x0 = ", self.x0, "\n"
                            "y0 = ", self.y0, "\n"
                                "x1 = ", self.x1, "\n"
                                            "y1 = ", self.y1, "\n"
                                                            "R = ",
                        self.R, "см.\n"
                          "r = ", self.r, "см.")


    def square_perimeter(self):
        P = round((2 * math.pi * (self.R + self.r)), 2)
        print("Периметр круга: ", P, ".")
        sleep(3)
        Sq = round((math.pi * (self.R ** 2 - self.r ** 2)), 2)
        print("Площадь круга: ", Sq, ".")

if __name__ == '__main__':
    flag = True
    while flag:
        f_x0 = 5
        print(f_x0)
        f_y0 = 8
        print(f_y0)
        f_x1 = 12
        print(f_x1)
        f_y1 = 20
        print(f_y1)
        f_R = abs(f_x0 - f_x1) / 2
        print("Внешний радиус (R):", f_R)
        f_r = int(input())
        circle1 = Circle(f_x0, f_y0, f_x1, f_y1, f_R)

