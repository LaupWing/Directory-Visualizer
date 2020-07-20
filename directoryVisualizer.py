import os

path = os.getcwd()

for path, subdirs, files in os.walk(path):
    print(path)
    print(subdirs)
    print(files)