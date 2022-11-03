import os

file_list = []


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


for file in files("./anekdot"):
    file_list.append(file)

anekdot_list = file_list[:]