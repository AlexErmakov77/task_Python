

import math
import sys


# функция возвращает массив координат точек
def xy_point_array(file_tochka):
    with open(file_tochka) as file:
        array_xy_point = [row.strip().split(" ") for row in file]
        return array_xy_point

# функция просмотра координат точек
def xy_point(array_xy_point):
    for inner in array_xy_point:
        print(inner[0])
        print(inner[1])
        return inner[0], inner[1]


# функция проверки где находится точка
def result_return(x_point, y_point, r_circle, tx_point, ty_point):

    #сместим центр координат , чтобы окр. была  в центре

    delta_x = 0 - x_point
    delta_y = 0 - y_point

    x_point = delta_x
    y_point = delta_y

    # смещаем точку относительно нового центра
    tx_point = tx_point + delta_x
    ty_point = ty_point + delta_y

    # считаем по координатам точки - гипотенузу потом сравним ее с радиусом окр.
    hypotenuse = math.sqrt(tx_point ** 2 + ty_point ** 2)

    # print(tx_point)
    # print(ty_point)
    # print(hypotenuse)

    if hypotenuse == r_circle:
        report = 0
        #print(report, "Точка на окружности")
    elif hypotenuse < r_circle:
        report = 1
        #print(report, "Точка внутри круга")
    else: # hypotenuse > r_circle:
        report = 2
        #print(report, "Точка снаружи круга")
    return report




if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Ошибка. Не переданы два файла, через пробел ")
    else:
        if len(sys.argv) < 3:
            print("Ошибка. Слишком мало параметров.")
            sys.exit(1)

        if len(sys.argv) > 3:
            print("Ошибка. Слишком много параметров.")
            sys.exit(1)

        if len(sys.argv) == 3:

            file_okr = sys.argv[1]
            file_dot = sys.argv[2]

            # print(file_okr)
            # print(file_dot)


            with open(file_okr) as file:

                for num_line, line in enumerate(file):

                    my_list_okr = line.split(" ")

                    if num_line == 0:
                        x_point = float(my_list_okr[0])
                        y_point = float(my_list_okr[1])
                    if num_line == 1:
                        r_circle = float(my_list_okr[0])

                # print("x_point=", x_point, "y_point=", y_point,"r_circle=", r_circle)


        # print("$$$", xy_point_array(file_dot))
        # print("$$$ len", len(xy_point_array(file_dot)))
        # print("%%% len ", xy_point_array(file_dot))
        #print(xy_point(xy_point_array(file_dot)))
        #print("count_point_file(file_dot)", count_point_file(file_dot))
        # print("array_xy_point q", q)


        q = xy_point_array(file_dot).copy()
        for i in q:

            tx_point = float(i[0])
            ty_point = float(i[1])
            #print("####  tx_point", tx_point)
            #print("##### ty_point", ty_point)

            print(result_return(x_point, y_point, r_circle, tx_point, ty_point))

