import re
hand = open('slide.txt')
myd = 'it was 1942 when i was 12 when 7 men went to war in 1945'
extra = re.findall('[0-9]+',myd)
print(extra)
for line in hand:
    line = line.strip()
extreme = re.findall('^13.+:', line)
print(extreme)
