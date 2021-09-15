import os
import fnmatch
import natsort

# 맥의 경우 ls-a 로 '.DS_Store' 파일 삭제 하고 사용

# JPG파일 리스트와 txt파일 리스트를 만든다.
jpgfiles_list = os.listdir('/Users/jwoh/Desktop/FileMatching-demo/jpg')
txtfiles_list = os.listdir('/Users/jwoh/Desktop/FileMatching-demo/txt')

# jpg files list를 str로 변환
withOutCommaJPG="".join(jpgfiles_list)
# jpg를 분리한다. 
newJPG = withOutCommaJPG.split('.jpg')
# txt files list를 str로 변환
withOutCommaTXT="".join(txtfiles_list)
# txt를 분리한다. 
newTXT = withOutCommaTXT.split('.txt')
# jpg 정렬 
jpgSorted_list = natsort.natsorted(newJPG)
# txt 정렬 
txtSorted_list = natsort.natsorted(newTXT)

# print(len(txtSorted_list))
# print(len(jpgSorted_list))
cnt = 0

# 일단 txt jpg 파일들을 모아놓고, txt파일이 많다고 가정
# txt < jpg 
# jpg list에 txt list를 대입한다. 
for item1 in txtSorted_list:
    if(item1 in jpgSorted_list):
        pass                
    else:
        print("jpg file Not in List",item1)

# jpg > txt
# txt list에 jpg list를 대입한다. 
# for item1 in jpgSorted_list:
#     if(item1 in txtSorted_list):
#         pass                
#     else:
#         print("Not in List",item1)



