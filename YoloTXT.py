# YOLO txt 파일, class 부분 숫자 바꾸는 코드
import os

# files 배열을 만든다.
files = []
# Add the path of txt folder
# 폴더 경로 설정 
path='/Users/jwoh/Desktop/chairTXT'
for i in os.listdir("/Users/jwoh/Desktop/chairTXT"):
    # 만약 .txt로 끝나는 파일 있으면,
    if i.endswith('.txt'):
        # files 배열에 추가한다
        files.append(i)

for item in files:
    # define an empty list
    # file_data 배열을 만든다.
    file_data = []

    # open file and read the content in a list
    # 파일을 열고 파일 리스트의 내용을 읽는다.
    with open(path+'/'+item, 'r') as myfile:
        for line in myfile:
            # remove linebreak which is the last character of the string
            # 각 라인마다 공백을 지운다.
            currentLine = line[:-1]
            data = currentLine.split(" ")

            # add item to the list
            # 다시 file_data 배열에 추가한다.
            file_data.append(data)
    
    # Decrease the first number in any line by one
    # 각 줄의 첫 번째 숫자를 +로 늘리거나 -로 줄인다.
    for i in file_data:
        # 만약 각 첫 라인의 첫 글자가 디지털문자라면,
        if i[0].isdigit():
            # temp에 원하는 숫자를 더하거나 뺀다.
            temp = float(i[0]) - 5
            i[0] = str(int(temp))

    # Write back to the file
    # 파일을 쓰기 모드로 연다.
    f = open(path+'/'+item, 'w')
    for i in file_data:
        res = ""
        for j in i:
            res += j + " "
        f.write(res)
        f.write("\n")
    f.close()