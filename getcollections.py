from sickle import Sickle

# force IPv4

import socket
import requests.packages.urllib3.util.connection as urllib3_cn

def allowed_gai_family():
    """
    https://github.com/urllib3/urllib3/blob/master/src/urllib3/util/connection.py
    """
    return socket.AF_INET

urllib3_cn.allowed_gai_family = allowed_gai_family

sickle = Sickle('http://api.bl.uk/metadata/oaipmh/v2/service')
wanted = ['EAP105', 'EAP570', 'EAP727', 'EAP529']
records = sickle.ListRecords(metadataPrefix='ead', set='bleadeap')
print('<records>')
record = records.next()
while record is not None:
    eadid = record.metadata['eadid'][0]
    if eadid[:6] in wanted:
        print(record)
    record = records.next()
print('</records>')