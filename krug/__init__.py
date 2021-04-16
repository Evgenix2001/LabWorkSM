import math
from time import sleep

class Circle:
    def __init__(self, x0, y0, x1, y1, R, r,):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.R = R
        self.r = r
        if self.x0 > 0 and self.y0 > 0 and self.x1 > 0 and self.y1 > 0 and self.x0 is None:
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
        x0 = 5
        print(x0)
        y0 = 8
        print(y0)
        x1 = 12
        print(x1)
        y1 = 20
        print(y1)
        R = abs(x0 - x1) / 2
        print("Внешний радиус (R):", R)
        r = 5
