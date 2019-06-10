def greeting(lang):
    if lang == 'es':
        print('You are Spanish')
    elif lang == 'fr':
        print('You are French')
    else:
        print('You are English')

person = input('Language: ')
greeting(person)
