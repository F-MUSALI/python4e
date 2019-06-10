import xml.etree.ElementTree as ET

data = '''
<person age = '25'>
    <name>MUSALI FRANCIS</name>
    <phone>+256704122678</phone>
    <location>KAMPALA</location>
</person>
'''
info = ET.fromstring(data)
print('Name:', info.find('name').text)
