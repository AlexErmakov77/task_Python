

import sys


# функция чтения данные из файла
def read_file(file_input):
    with open(file_input) as file:
        array_xy_point = [row.strip() for row in file]

        return array_xy_point

if __name__ == "__main__":

    if len (sys.argv) < 2:
        print ("Ошибка. Не передано название файла в качестве параметра .")
        sys.exit (1)

    if len (sys.argv) > 2:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    if len(sys.argv) == 2:

        # обращаюсь к read_file возвращаю массив, и привожу содержимое к int
        arr_input = [int(numeric_string) for numeric_string in read_file(sys.argv[1]).copy()]
        # print("@@@***", arr_input)

        # рачет количества шагов
        result = sorted(arr_input)[len(arr_input) // 2]
        print(sum(abs(v - result) for v in arr_input))