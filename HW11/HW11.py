import datetime
import time
import csv
import json

# TASK 1
class custom_open_file:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.mode = mode
        self.file_name = file_name
    def __enter__(self):
        self.logging('OPEN')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logging('CLOSE')
        self.file.close()
    def logging(self, param:str):
        with open('log.txt', 'a+') as ff:
            ff.write(str(datetime.datetime.now()))
            ff.write(' ')
            ff.write(self.file_name)
            ff.write(' ')
            ff.write(f'{param}\n')

with custom_open_file('murmur.txt', 'r') as f:
    time.sleep(2)
    print(f.read())

with custom_open_file('lalala.txt', 'w') as f:
    f.write('Romantical things')

with custom_open_file('tururu.txt', 'w') as f:
    f.write('Little kitty')

# TASK 2
with open('log.txt', 'r') as file:
    with open('log.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Date', 'Time', 'File', 'Status'])
        for line in file:
            writer.writerow(line.split())

# TASK 3
copy = []
names = [] # імена файлів, які маємо
data = {} # результуючий
with open('log.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
        copy.append(line)
        if line[2] not in names:
            names.append(line[2]) # збереження імен файлів окремо
names.pop(0) # видаляємо головний рядок
copy.pop(0)
data = dict.fromkeys(names) # створюється словник з ключами - іменами файлів
for k in names:
    data[k] =  {"count":0, "last_time_opened":""} # ініціалізація словника

for j in names:
    for i in copy:
        if i[2] == j and i[3] == 'OPEN':
            data[j]["count"] += 1
            data[j]["last_time_opened"] = str(i[0]) + ' ' + str(i[1])
print('Data: ', data)

json_data = json.dumps(data) # конвертація в JSON

print('JSONData :', json_data)