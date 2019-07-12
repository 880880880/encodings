import re

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files):
    os_prod_list=[]
    os_name_list=[]
    os_code_list=[]
    os_type_list=[]
    main_data=[['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],os_prod_list,os_name_list,os_code_list,os_type_list]
    for file in files:
        with open(file) as currentfile:
            for line in currentfile:
                if re.match(r'Изготовитель системы', line): os_prod_list.append(line.split(':')[-1].strip())
                if re.match(r'Название ОС',line): os_name_list.append(line.split(':')[-1].strip())
                if re.match(r'Код продукта', line): os_code_list.append(line.split(':')[-1].strip())
                if re.match(r'Тип системы', line): os_type_list.append(line.split(':')[-1].strip())
    return main_data


result = get_data(files)
print(result)
