import os

# print(os.getcwd())

f = os.popen("dir")

print(f.read())