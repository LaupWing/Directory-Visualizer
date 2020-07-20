import os

unwanted = ['.git', 'node_modules']

path = os.getcwd()
tree = {
    "root": os.path.basename(path),
    "directories": [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))],
    "files": [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
}

print(tree)
# for root, dirs, files in os.walk(os.getcwd()):
#     base = os.path.basename(root)
#     dirs[:] = list(filter(lambda x: x not in unwanted, dirs))
#     tree = {
#         "root": base,
#         "directories": dirs,
#         "files": files
#     }
#     # print(tree)
#     if root in tree["directories"]:
#         print('go in')
#     # if base == 'inner_test2':
#     #     print('skip')
#     print()
#     print(base)
#     print(dirs)
#     print(files)
#     print()