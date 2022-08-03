# TASK 3 (з зірочкою)
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }

data = {}

import csv
with open('log.csv', 'r') as csv_file:
    file_list = []
    count = 0
    date = ''
    time = ''
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
        if line[2] not in file_list:
            file_list.append(line[2])
        print(line)
        if line[-1] == 'OPEN':
            count += 1
            date = str(line[0])
            time = str(line[1])
    file_list.pop(0) # прибираємо голову таблиці

    # data = dict.fromkeys([file_list])
    print('Open count: ', count)
    print('Date: ', date)
    print('Time: ', time)
    print('file_list: ', file_list)
    print('Data: ', data)