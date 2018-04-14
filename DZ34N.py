def check_values(A1, A2, A3, A4):
    '''
    По свойству диагоналей четырехугольника ABCD — параллелограмм, 
    если координаты середин отрезков АС и BD, совпадают
    '''
    x1 = (A1['x'] + A3['x']) / 2
    x2 = (A2['x'] + A4['x']) / 2
    y1 = (A1['y'] + A3['y']) / 2
    y2 = (A2['y'] + A4['y']) / 2

    if (x1 == x2 and y1 == y2):
        return True
    else:
        return False

def input_point(point_name='A'):
    point = list(map(
        float,
        input(f"Type {point_name} coords [x,y]: ").split(',')
    ))
    print(point)
    return {'x': point[0], 'y': point[1]}

a1 = input_point('A1')
a2 = input_point('A2')
a3 = input_point('A3')
a4 = input_point('A4')

print(check_values(a1, a2, a3, a4))