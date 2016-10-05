# http://stackoverflow.com/questions/39870942/parsing-xml-in-python-with-multiple-tags


import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('info.xml').getroot()

# for stationsnamens in e.findall('Station'):
    # try:
        # syn = stationsnamens.find('Synoniemen/Synoniem').text
        # print(syn)
    # except:
        # print(Exception)

for stationsnamens in e.findall('Station'):
    try:
        syn = stationsnamens.find('Synoniemen')
        for synoniem in syn:
            print(synoniem.text)
    except:
        print(Exception)

