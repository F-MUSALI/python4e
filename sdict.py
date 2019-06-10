count = dict()
names = ['lisa', 'grace','elsie','becky','lydia','lydia']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)
