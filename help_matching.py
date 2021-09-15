import os

path = './help_data'
file_list = os.listdir(path)

remove_file_name = []

for file_name in file_list:
    name, ext = os.path.splitext(file_name)
    if ext == '.txt' and name != 'classes':
        if os.path.getsize(file_name)  == 0:
            remove_file_name.append(name)
            os.remove(file_name)
            print(file_name, '삭제')

for file_name in file_list:
    name, ext = os.path.splitext(file_name)
    if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
        for remove_name in remove_file_name:
            if remove_name == name:
                os.remove(file_name)
                print(file_name, '삭제')