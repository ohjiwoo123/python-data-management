import os

path = './help_data'
file_list = os.listdir(path)

img_count_total = 0
box_count = [0, 0, 0, 0, 0, 0, 0]
img_flag = [True, True, True, True, True, True, True]
img_count = [0, 0, 0, 0, 0, 0, 0]
class_name = ['person', 'chair', 'suitcase', 'cart', 'trashbag', 'info vert', 'info horizen']


for file_name in file_list:
    name, ext = os.path.splitext(file_name)

    if ext == '.txt' and name != 'classes':
        with open(path + '/' + file_name, 'r') as my_file:
            img_count_total +=1
            my_file_lines = my_file.readlines()
            for line in my_file_lines:
                for i in range(len(class_name)):
                    if (line[0] == str(i)):
                        if(img_flag[i]):
                            img_count[i] += 1
                            img_flag[i] = False
                        box_count[i] += 1
        for i in range(len(class_name)):
            img_flag[i] = True


print('총 이미지 개수 : ', img_count_total)
for i in range(len(class_name)):
    print('클래스 ' + class_name[i] + '의 박스 개수: ', box_count[i], '개')
    print('클래스 ' + class_name[i] + '의 이미지 개수: ', img_count[i], '장')

                    
                
                