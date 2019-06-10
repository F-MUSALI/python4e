import json
data = '''{
    "name" : "musali",
    "phone" : {
        "type" : "intl",
        "number" : "0704122678"
    },
    "email" : {
        "hide" : "yes"
    },
    "location" : "kampala"
}
'''
extra = json.loads(data)
print('NAME:', extra["name"])
print('PHONE:', extra["phone"])
print('EMAIL:', extra["email"]["hide"])
print('LOCATION:', extra["location"])
