import sys

print(sys.version)
# 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]

def get_python_executable_path():
    return sys.executable


print("The path to the Python executable is:", get_python_executable_path())

#  C:\Users\<<username>>\AppData\Local\Programs\Python\Python314\python.exe

