"""

write is always dangerous..it may overwrite all the old contents

"""
with open("python.txt", 'w') as f:
    f.write("Python is awesome!!! \n")
    f.write("I love python!!!")
