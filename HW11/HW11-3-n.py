import csv
data = {}
file_list = []
with open('log.csv', 'r') as csv_file:
    count = 0
    date = ''
    time = ''
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
        print(line)
        if line[2] not in data.keys():
            if line[3] == 'OPEN':
                data[line[2]] = {'open_count' : 1}

file_list.pop(0) # знімаємо голову
print(file_list)
