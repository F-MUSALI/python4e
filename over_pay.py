
def over(Hours, Rate):
    print('Your Details: ', Hours, Rate)
    if Hours > 40:
        Hours = Hours * 1.5
        pay = Rate * Hours
    else:
         pay = Hours * Rate
    return pay

Hour = input('Hours: ')
Rat = input('Rate: ')
Hour = float(Hour)
Rat = float(Rat)

pay = over(Hour, Rat)
print('Your pay: ', pay)
