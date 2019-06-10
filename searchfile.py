import re
filer = open('slide.txt')
for line in filer:
    line = line.strip()
    if re.search('army', line):
        print(line)
