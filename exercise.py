total = 0
num = 0.0
while True:
    user = input('Enter No: ')
    if user == 'done':
        break
    try:
        fanuser = int(user)
    except:
        print('invalid input')
        continue
    print(fanuser)
    num = num + 1
    total = total + fanuser
print('Total:',total, 'Number: ',num, 'avg: ',total/num)
print('we are done')
