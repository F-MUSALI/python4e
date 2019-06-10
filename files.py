fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Sorry, system failed to open this file', fname)
    quit()
count = 0
for lines in fhand:
    lines = lines.strip()
    count = count + 1
    if not 'support' in lines:
        continue
    print(lines.upper())
print('No:',count)
