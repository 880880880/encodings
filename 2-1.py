import re
import csv

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files):
    os_prod_list=[]
    os_name_list=[]
    os_code_list=[]
    os_type_list=[]
    main_data=[[u'Изготовитель системы', u'Название ОС', u'Код продукта', u'Тип системы']]
    for file in files:
        with open(file) as currentfile:
            for line in currentfile:
                if re.match(r'Изготовитель системы', line): os_prod_list.append(line.split(':')[-1].strip())
                if re.match(r'Название ОС',line): os_name_list.append(line.split(':')[-1].strip())
                if re.match(r'Код продукта', line): os_code_list.append(line.split(':')[-1].strip())
                if re.match(r'Тип системы', line): os_type_list.append(line.split(':')[-1].strip())
    for x in range(len(files)):
        main_data.append([os_prod_list[x],os_name_list[x],os_code_list[x],os_type_list[x]])
    return main_data

def write_csv(outputfile,files):
    result = get_data(files)
    with open(outputfile, 'w', encoding='utf-8') as file:
        filewriter = csv.writer(file)
        for row in result:
            filewriter.writerow(row) # пишем csv
    for i in result: print(i) # и на экран дублируем вывод

outputfile='output.csv'
write_csv(outputfile,files)



