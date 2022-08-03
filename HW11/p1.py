# f = open('./murmur.txt')
#print(f.read(-1)) # читаємо певну к-ть символів. -1, чи пустота - читання всього файлу.

# print(f.readline())
# print(f.readline()) # читаємо по рядку, там ітератор, тому кожного разу буде новий рядок.

# print(f.fileno()) # номер файлика в таблиці-дескрипторі

# for line in f:
#     print(line, end = '') # те саме, але просунутіше
# f.close() # закривайте відкритий файл і буде вам нормально

# try:
#     for line in f:
#         print(line)
# finally:
#     f.close()  # щоб гарантовано закрити файл, навіть коли закрашиться код

# with open('murmur.txt') as f: #Контекстний менеджер; ця конструкція сама закриє файл, і паритися нам не доведеться
#     for line in f:
#         print(line)

# class custom_open_file: # кастомний контекстний менеджер
#     def __init__(self, file_name):
#         print('--INIT is working')
#         self.file = open(file_name)
#     def __enter__(self):
#         print('--ENTER is working')
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('--EXIT is working')
#         self.file.close()
#
# with custom_open_file('murmur.txt') as f:
#     print('Context manager is running')
#     print(f.read())
# print('End')

# with open('murmur.txt', 'w') as f: # файл відкрито для перезапису
#     f.write('New line cinema')
#     f.write('Another line inc.')

# with open('murmur.txt', 'a') as f: # файл відкрито для дозапису, не стирає нічого, дописує
#     f.write('Something new')

# with open('murmur.txt', 'w+') as f: # файл відкрито запису та читання
#     f.write('Something new')
#     f.seek(0) # поставимо курсор на початок
#     print(f.tell()) # покаже нам позицію курсора
#     print(f.read())

# import os
# if os.path.exists('wondersex.txt'): # перевірка наявності
#     os.remove('wondersex.txt') # видалення
# else:
#     print('So file does not exist')
# os.rmdir('125') # видалення каталогу
