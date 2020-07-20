import os


for root, dirs, files in os.walk(os.getcwd()):
    base = os.path.basename(root)
    if base == 'inner_test2':
        print('skip')
    print(files)