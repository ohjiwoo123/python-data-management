import os
import fnmatch
import natsort

# 맥의 경우 ls-a 로 '.DS_Store' 파일 삭제 하고 사용

# JPG파일 리스트와 txt파일 리스트를 만든다.
jpgfiles_list = os.listdir('/Users/jwoh/Desktop/FileMatching-demo/jpg')
txtfiles_list = os.listdir('/Users/jwoh/Desktop/FileMatching-demo/txt')

withOutCommaJPG="".join(jpgfiles_list)
newJPG = withOutCommaJPG.split('.jpg')
# print(newJPG)
withOutCommaTXT="".join(txtfiles_list)
newTXT = withOutCommaTXT.split('.txt')
jpgSorted_list = natsort.natsorted(newJPG)
txtSorted_list = natsort.natsorted(newTXT)

print(len(txtSorted_list))
cnt = 0

for item1 in jpgSorted_list:
    if(item1 in txtSorted_list):
        pass                
    else:
        print("Not in List",item1)


# while cnt < len(txtSorted_list):
#     for item1 in txtSorted_list:
#         for item2 in jpgSorted_list:
#             if(item1 in jpgSorted_list):
#                 cnt += 1
#                 pass                
#             else:
#                 print("Not in List",item1)
#                 cnt += 1