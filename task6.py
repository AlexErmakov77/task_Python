#Дано 2 строки, переданные через пробел. Вернуть строковое значение 'true', если строки являются анаграммами, иначе вернуть 'false'.


# put your python code here
a, b = input().split()

if len(a) != len(b):
    print("false")
else:

    dict_a = {}
    dict_b = {}

    for i in a:
        dict_a[i] = i
    for i in b:
        dict_b[i] = i

    if sorted(dict_a.items(), key=lambda x: x[0]) == sorted(dict_b.items(), key=lambda x: x[0]):
        print("true")
    else:
        print("false")
