# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class isosceles_trapezoid():
    def __init__(self, coordsA, coordsB, coordsC, coordsD):
        self.__coordsA = coordsA
        self.__coordsB = coordsB
        self.__coordsC = coordsC
        self.__coordsD = coordsD
    @property
    def xa(self):
        return int(self.__coordsA[0])
    @property
    def xb(self):
        return int(self.__coordsB[0])
    @property
    def xc(self):
        return int(self.__coordsC[0])
    @property
    def xd(self):
        return int(self.__coordsD[0])
    @property
    def ya(self):
        return int(self.__coordsA[1])
    @property
    def yb(self):
        return int(self.__coordsB[1])
    @property
    def yc(self):
        return int(self.__coordsC[1])
    @property
    def yd(self):
        return int(self.__coordsD[1])
    @property
    def test(self):
        if self.len_ab == self.len_cd or self.len_bc == self.len_da:
            return True
    @property
    def tra_perimetr(self):
        perimeter = self.len_ab + self.len_bc + self.len_cd + self.len_da
        return perimeter
    @property
    def len_ab(self):
        import math
        ab = math.sqrt((self.xb - self.xa) ** 2 + (self.yb - self.ya) ** 2)
        return ab
    @property
    def len_bc(self):
        import math
        bc = math.sqrt((self.xc - self.xb) ** 2 + (self.yc - self.yb) ** 2)
        return bc
    @property
    def len_cd(self):
        import math
        cd = math.sqrt((self.xd - self.xc) ** 2 + (self.yd - self.yc) ** 2)
        return cd
    @property
    def len_da(self):
        import math
        da = math.sqrt((self.xa - self.xd) ** 2 + (self.ya - self.yd) ** 2)
        return da
    @property
    def tra_area(self):
        import math
        area = (self.len_bc + self.len_da) / 2 * \
            math.sqrt(self.len_ab ** 2 - ((self.len_da - self.len_bc) ** 2) / 4)
        return area
trapezoid1 = isosceles_trapezoid([0, 0], [0, 2], [2, 2], [2, 0])
print(trapezoid1.tra_perimetr)
print(trapezoid1.tra_area)