

import sys
import json

# функция возврата значения value из файла values.json по запрашиваемому id
def return_values(input_values, id_input_values):
    #print(input_values)
    #print(id_input_values)
    for i in range(len(input_values["values"])):

        #print(data_values["values"][i]["id"])
        #print(data_values["values"][i]["value"])
        id_values = data_values["values"][i]["id"]
        if id_input_values == id_values:

            #print(data_values["values"][i]["value"])

            res_value = data_values["values"][i]["value"]

    return res_value

# функция возвращает список из словаря по ключам "tests" or  "values"
def return_list(input_tests):

    for k, v in input_tests.items():
        # print(f"\nKey: {k}")
        # print(f"\nValue: {v}")
        if k == "tests" or k == "values":
            return v


# функция присваивает значение "value" по соответсвию id , из файла values.json
# и проверяет есть ли ключ "values", если да,то рекурсивный вызов
def vlog_dict(input_dict):

    for i in range(len(input_dict)):

        #return_list(data_tests)[i]["value"] = return_values(data_values, return_list(data_tests)[i]["id"])
        input_dict[i]["value"] = return_values(data_values, return_list(data_tests)[i]["id"])

        if (input_dict[i]).get("values"):
            vlog_dict(return_list(input_dict[i]))




if __name__ == "__main__":

    if len (sys.argv) < 3:
        print ("Ошибка. Слишком мало параметров.")
        sys.exit (1)

    if len (sys.argv) > 3:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    if len(sys.argv) == 3:

        file_tests = sys.argv[1]
        print("file_tests: ", file_tests)

        file_values = sys.argv[2]
        print("file_values: ", file_values)


        with open(file_tests) as json_file:
            data_tests = json.load(json_file)

        with open(file_values) as json_file:
            data_values = json.load(json_file)

            #print("********")
            #print(len(data_values["values"]))
            #print("********")
            #print(return_values(data_values, 2), "### response return_values ###")
            #print(return_list(data_tests), "### response test ###")


            # сохранение результата обработки в файле report.json

            report_json = json.dumps(return_list(data_tests))

            with open("report5.json", "w") as my_file:
                my_file.write(report_json)

