import datetime
import time

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
import csv
with open('log.txt', 'r') as file:
    with open('log.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Date', 'Time', 'File', 'Status'])
        for line in file:
            writer.writerow(line.split())

# TASK 3
data = {}
with open('log.csv', 'r') as csv_file:
    file_list = []
    count = 0
    date = ''
    time = ''
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
        print(line)
        if line[2] not in file_list:
            file_list.append(line[2])
        if line[-1] == 'OPEN':
            count += 1
            date = str(line[0])
            time = str(line[1])
    print('Open count: ', count)
    print('Date: ', date)
    print('Time: ', time)