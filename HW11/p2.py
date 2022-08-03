class custom_open_file: # кастомний контекстний менеджер
    def __init__(self, file_name, mode):
        print('--INIT is working')
        self.file = open(file_name, mode)
        self.mode = mode
        self.file_name = file_name
    def __enter__(self):
        print('--ENTER is working')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('--EXIT is working')
        self.file.close()
        with  open(self.file_name, 'a+') as f:
            f.seek(0)
            # print(f.readlines()[-1])
            if f.readlines()[-1] != 'Control line':
                f.write('\nControl line')


with custom_open_file('murmur.txt', 'r') as f:
    print(f.read())