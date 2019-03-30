import csv
from xml.dom import minidom

doc = minidom.parse("sickle.xml")

with open('eap.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    titlesLine = [
        'level',
        'id',
        'link',
        'notBefore',
        'notAfter',
        'lang',
        'script',
        'userrestriction',
        'title',
        'originalsloc',
        'scopecontent0',
        'scopecontent1'
    ]
    csv_writer.writerow(titlesLine)
    records = doc.getElementsByTagName("record")
    for record in records:
        infolist = []
        archdesc = record.getElementsByTagName("metadata")[0].getElementsByTagName("ead")[0].getElementsByTagName("archdesc")[0]
        level = archdesc.getAttribute("level")
        infolist.append(level)
        idwithslashes = archdesc.getElementsByTagName("unitid")[0].firstChild.nodeValue
        infolist.append(idwithslashes)
        idforlink = idwithslashes.replace('/','-')
        if level == 'file':
            infolist.append('https://eap.bl.uk/archive-file/'+idforlink)
        else:
            infolist.append('https://eap.bl.uk/collection/'+idforlink)
        dates = archdesc.getElementsByTagName("unitdate")[0].getAttribute("normal").split('/')
        infolist.append(dates[0])
        if (len(dates) > 1):
            infolist.append(dates[1])
        else:
            infolist.append("")
        langmaterial = archdesc.getElementsByTagName("langmaterial")[0]
        infolist.append(langmaterial.getElementsByTagName("language")[0].getAttribute("langcode"))
        infolist.append(langmaterial.getElementsByTagName("language")[1].getAttribute("scriptcode"))
        userestrictL = archdesc.getElementsByTagName("userestrict")
        if userestrictL:
            infolist.append(userestrictL[0].getElementsByTagName("p")[0].firstChild.nodeValue)
        else:
            infolist.append("")
        unittitleL = archdesc.getElementsByTagName("unittitle")
        if unittitleL:
            infolist.append(unittitleL[0].firstChild.nodeValue)
        else:
            infolist.append("")
        originalslocL = archdesc.getElementsByTagName("originalsloc")
        if originalslocL:
            infolist.append(originalslocL[0].getElementsByTagName("p")[0].firstChild.nodeValue)
        else:
            infolist.append("")
        scopecontentL = archdesc.getElementsByTagName("scopecontent")
        if scopecontentL:
            scopecontent = scopecontentL[0]
            pL = scopecontent.getElementsByTagName("p")
            if pL:
                infolist.append(pL[0].firstChild.nodeValue)
            else:
                infolist.append("")    
            if len(pL) > 1 and pL[1].firstChild:
                infolist.append(pL[1].firstChild.nodeValue)
            else:
                infolist.append("")
        else:
            infolist.append("")
            infolist.append("")
        csv_writer.writerow(infolist)

