# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle():
    def __init__(self, coordsA, coordsB, coordsC):
        self.coordsA = list(coordsA)
        self.coordsB = list(coordsB)
        self.coordsC = list(coordsC)
    def tri_area(self):
        import math
        area = math.fabs((int(self.coordsA[0])-int(self.coordsC[0]))*(
            int(self.coordsB[1])-int(self.coordsC[1]))-(
            int(self.coordsB[0])-int(self.coordsC[0]))*(
            int(self.coordsA[1])-int(self.coordsC[1]))/2)
        return area
    def tri_hight(self, vertex):
        import math
        if vertex == 'A':
            V = self.coordsA
            O1 = self.coordsB
            O2 = self.coordsC
        elif vertex == 'B':
            V = self.coordsB
            O1 = self.coordsA
            O2 = self.coordsC
        else:
            V = self.coordsC
            O1 = self.coordsB
            O2 = self.coordsA
        hight = (math.fabs((int(O1[1]) - int(O2[1])) * int(V[0]) +
            (int(O2[0]) - int(O1[0])) * int(V[1]) + \
            int(O1[0]) * int(O2[1]) - int(O2[0]) * int(O1[1]))) / \
            (math.sqrt((int(O1[1]) - int(O2[1])) ** 2 + \
            (int(O2[0]) - int(O1[0])) ** 2))
        return hight
    def tri_perimeter(self):
        import math
        perimeter = math.sqrt(int(self.coordsA[0]) ** 2 + int(self.coordsA[1]) ** 2) + \
            math.sqrt(int(self.coordsB[0]) ** 2 + int(self.coordsB[1]) ** 2) + \
            math.sqrt(int(self.coordsC[0]) ** 2 + int(self.coordsC[1]) ** 2)
        return perimeter
    @property
    def xa(self):
        return self.coordsA[0]
    @xa.setter  
    def xa(self, xa):
        self.coordsA = [xa, self.coordsA[1]]




tri1 = Triangle([1, 4], [-7, 5], [6, 6]) 
print(tri1.tri_area())
print(tri1.tri_hight('C'))
print(tri1.tri_perimeter())
print(tri1.coordsA)
tri1.xa = 5
print(tri1.xa)
