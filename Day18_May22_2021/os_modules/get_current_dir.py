import os

current_dir = os.getcwd()
print(current_dir)

os.chdir("/Users/bharathdasaraju/git/python_practise/Day18_May22_2021/demos")
print(os.getcwd())

with open("test.txt", 'w') as f:
    f.write("This is a test file")

