text = input('Enter file: ')
if len(text) < 1 : text = 'slice.txt'
handle = open(text)
dic = dict()
for line in handle:
    line = line.strip()
    #print(line)
    wordray = line.split()
    #print(wordray)
    for w in wordray:
        if w in dic: dic[w] = dic[w] + 1
        else: dic[w] = 1
        print(w, dic[w])
print(dic)
