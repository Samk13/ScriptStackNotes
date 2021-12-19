import os
from contextlib import contextmanager

# cwd = os.getcwd()
# print(cwd)
# os.chdir("D:\Workspace\code\Python")
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(path):
    try:
        cwd = os.getcwd()
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)


with change_dir("D:\Workspace\code\Python"):
    print(os.listdir())
with change_dir("D:\Workspace\code"):
    print(os.listdir())
