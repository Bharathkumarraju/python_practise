marks = {}.fromkeys(['maths', 'english', 'science', 'biology', 'physics', 'anatomy'], 0)
print(marks)

for item  in marks.items():
    print(item)

print(list(sorted(marks.items())))
print(list(sorted(marks.keys())))

print(dict(sorted(marks.items())))