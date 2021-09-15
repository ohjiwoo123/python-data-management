# yolo 이미지 박스 칠 때, txt파일 크기가 0인 것을 삭제하는 프로그램 
import os

# 경로 설정 
path = './help_data'
file_list = os.listdir(path)

# 삭제할 파일 빈 리스트로 선언 
remove_file_name = []

# TXT 파일 삭제 중복문
for file_name in file_list:
    # 파일 이름 및 확장자 split으로 분리
    name, ext = os.path.splitext(file_name)
    if ext == '.txt' and name != 'classes':
        # 만약 txt 파일 크기가 0이라면
        if os.path.getsize(file_name)  == 0:
            # 아까 정의한 빈 리스트에 name을 추가한다. 
            remove_file_name.append(name)
            # 크기가 0인 txt 파일 삭제 
            os.remove(file_name)
            print(file_name, '삭제')

# jpg, jpeg, png 파일 삭제 중복문 
for file_name in file_list:
    # 파일 이름 및 확장자 split으로 분리
    name, ext = os.path.splitext(file_name)
    # 만약 확장자가 jpg, jpeg, png라면 
    if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
        # txt 크기가 0인 확장자를 뺀 파일 이름 사진 파일 삭제 
        for remove_name in remove_file_name:
            if remove_name == name:
                os.remove(file_name)
                print(file_name, '삭제')