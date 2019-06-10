found = False
print('searching...')
for value in [5,3,8,3,8,6,9,5,7,4,1]:
    if value == 6:
        found = True
        yeah = value
        print(found, yeah)
    else:
        found = False
        print(found, value)
print('yeah we found it and its',yeah)
