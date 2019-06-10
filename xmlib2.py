import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user n = '2'>
            <id>ST:105</id>
            <name>MUSALI</name>
        </user>
        <user n = '3'>
            <id>ST:204</id>
            <name>FRANCIS</name>
        </user>
    </users>
</stuff>
'''
extra = ET.fromstring(data)
lst = extra.findall('users/user')
print('no_of_users:', len(lst))

for line in lst:
    print('Number:', line.get('n'))
    print('ID:', line.find('id').text)
    print('Name:', line.find('name').text)
