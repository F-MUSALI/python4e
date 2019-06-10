myfile = open('C:/Users/musali/Documents/icp_20190408_145018.txt')

for line in myfile:
    line = line.strip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'Vendor':
        continue
    print(words[2], words[3])
