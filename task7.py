#На вход подается натуральное число n (0 < n <= 1000). Вернуть строковое значение 'true', если число простое, иначе вернуть 'false'.
n = int(input())

if n > 1 and (n <= 1000):
    k = 0
    for i in range(2, n ):
        if (n % i == 0):
            k = k+1
    if (k ==0):
        print("true")
    else:
        print("false")
else:
    print("false")

