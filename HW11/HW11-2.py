import csv
with open('log.txt', 'r') as file:
    with open('log.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Date', 'Time', 'File', 'Status'])
        for line in file:
            writer.writerow(line.split())