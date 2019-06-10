greeting = 'hello'
try:
    greeting = int('hello')
except:
    greeting = 'what is that!!!'
print('wow ', greeting)

greeting = '123'
try:
    greeting = int(greeting)
except:
    greeting = -1
print('now thats ', greeting)
