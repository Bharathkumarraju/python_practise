"""
writelines() --> writes a list to file
"""

with open("javascript.txt", 'w') as f:
    lines = ["Js is also awesome", "\nJS is my second favourite language"]
    f.writelines(lines)

