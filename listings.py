newlist = list()
while True:
    new = input('Enter No:')
    if new == 'done': break
    value = float(new)
    newlist.append(value)
try:
    ave = sum(newlist) / len(newlist)
    print('Sum: ',sum(newlist),'Average: ', ave)
except:
    print('no values!!')
