Hours = input('Hours: ')
Rate = input('Rate: ')
try:
    Hours = int(Hours)
    Rate = int(Rate)
    Pay = Hours * Rate
    print('Your Pay: ', Pay)
except:
    print('are you serious right now!!, enter numeric data only')
