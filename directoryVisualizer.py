import os

unwanted = ['.git', 'node_modules']

for root, dirs, files in os.walk(os.getcwd()):
    base = os.path.basename(root)
    dirs[:] = list(filter(lambda x: x not in unwanted, dirs))
    # if base == 'inner_test2':
    #     print('skip')
    print()
    print(base)
    print(dirs)
    print(files)
    print()