

import sys

if __name__ == "__main__":
    if len (sys.argv) == 1:
        print ("Ошибка. Не переданы два числа, через пробел ")
    else:
        if len (sys.argv) < 3:
            print ("Ошибка. Слишком мало параметров.")
            sys.exit (1)

        if len (sys.argv) > 3:
            print ("Ошибка. Слишком много параметров.")
            sys.exit (1)

        if int(sys.argv[1]) < int(sys.argv[2]):
            print("Ошибка. длина массива меньше пути обхода.")
            sys.exit(1)

        if len(sys.argv) == 3 and int(sys.argv[1]) >= int(sys.argv[2]):

            n = int(sys.argv[1])
            m = int(sys.argv[2])
            one_List = m * [int(i) for i in range(1, n + 1)]
            two_List = [' ']
            three_List = []
            cnt = 0
            while two_List[-1] != 1:
                two_List.clear()
                for j in range(cnt, m + cnt):
                    two_List.append(one_List[j])
                    cnt += 1
                two_List_copy = two_List.copy()
                three_List.append(two_List_copy)
                cnt -= 1
            for k in range(len(three_List)):
                print(three_List[k][0], end='')
            print('\n')