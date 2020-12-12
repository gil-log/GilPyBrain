# 파일 함수

path = "D:/새파일.txt"

with open(path, 'w') as file:
    file.write("Gillog FileIOFunction End")


#
# file = open(path, 'a')
#
# for index in range(11, 21):
#     content = "인덱스 %d \n" %index
#
#     file.write(content)
#
# file.close()
#

# file = open(path + "/새파일.txt", 'w')
#
# for index in range(1, 11):
#     content = "인덱스 %d \n" %index
#
#     file.write(content)
#
# file.close()