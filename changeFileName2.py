import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = '/Users/jwoh/Desktop/chair241'
file_names = os.listdir(file_path)

i = 0


for name in file_names:
    src = os.path.join(file_path, name)
    rename = src.replace('(','')
    rename2 = rename.replace(')','')
    rename3 = rename2.replace(' ','')
    print(rename3)

    # dst = "outlet" + str(i) + '.jpg'
#     dst = os.path.join(file_path, dst)
#     os.rename(src, dst)
#     i += 1