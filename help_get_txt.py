# yolo 박스 친 txt파일을 읽어서, 앞에 클래스 숫자를 count하고, 박스 개수 및 이미지 개수를 count하는 코드
import os

# 경로 설정 
path = './help_data'
file_list = os.listdir(path)

# 이미지 총 개수 0으로 선언
img_count_total = 0
# box 개수 count 총 7개 리스트에 0으로 선언
box_count = [0, 0, 0, 0, 0, 0, 0]
# img_flag = 리스트 안에 True로 선언 
img_flag = [True, True, True, True, True, True, True]
# 이미지 개수 리스트 0 으로 선언 
img_count = [0, 0, 0, 0, 0, 0, 0]
# 클래스 person, chair,  suitcase, cart, trashbag, info_ver, info_horizon
class_name = ['person', 'chair', 'suitcase', 'cart', 'trashbag', 'info vert', 'info horizon']


for file_name in file_list:
    # 이름, 확장자 분리 
    name, ext = os.path.splitext(file_name)
    # 확장자가 txt이고 파일 이름이 classes가 아니라면 
    if ext == '.txt' and name != 'classes':
        # txt 파일을 연다
        with open(path + '/' + file_name, 'r') as my_file:
            # 이미지 총 개수를 1개 늘린다. 
            img_count_total +=1
            # txt 파일의 line을 읽는다.
            my_file_lines = my_file.readlines()
            # lines들을 읽은 것 안에 반복 
            for line in my_file_lines:
                # class_name 수 만큼 반복
                for i in range(len(class_name)):
                    # 라인에 처음 등장하는 것이 문자라면 
                    if (line[0] == str(i)):
                        # ??
                        if(img_flag[i]):
                            # img_count +1 추가 
                            img_count[i] += 1
                            # flag = False 
                            img_flag[i] = False
                        # box_count +1 추가
                        box_count[i] += 1
        # img_flag -> True 
        for i in range(len(class_name)):
            img_flag[i] = True


print('총 이미지 개수 : ', img_count_total)
# 각 클라스 이미지 박스 개수 출력
# 각 클라스가 포함 된 각각의 이미지 개수 출력  
for i in range(len(class_name)):
    print('클래스 ' + class_name[i] + '의 박스 개수: ', box_count[i], '개')
    print('클래스 ' + class_name[i] + '의 이미지 개수: ', img_count[i], '장')

                    
                
                