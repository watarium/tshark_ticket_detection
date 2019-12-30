import time, datetime, threading
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


cipher = '4a:25:b7:26:47:d3:29:67:14:58:e6:48:e2:0a:8e:5f:6d:f1:67:fe:4a:1d:19:cf:30:80:2e:a2:c4:5a:65:77:20:66:28:ef:03:5e:88:b7:c4:fb:ba:8b:e5:c6:1d:b1:f1:94:7a:11:8b:d7:06:be:49:b7:3a:29:7b:7e:23:ae:5f:37:19:ff:6a:24:d3:60:fd:24:ac:96:38:dd:e1:8b:75:7a:80:20:88:80:8d:d3:b0:a9:8e:c6:9b:14:7f:5e:9a:3e:55:75:af:98:36:e7:fc:d5:aa:4e:08:5a:63:f4:60:45:22:95:e1:ca:09:bd:de:c1:13:b0:31:9c:d2:70:84:e3:59:25:f1:32:8a:f0:bb:b3:c8:ff:6a:e3:fd:35:80:11:92:9e:c3:61:c9:35:c4:9f:64:b0:96:66:1c:36:ac:01:9c:74:44:3c:af:9e:fb:e0:f0:a2:3d:ab:d5:03:6d:39:a7:ca:14:41:cf:e0:c1:f3:4b:f1:50:6e:1e:98:62:67:53:12:b9:43:b7:84:21:fe:64:c0:7d:ca:fe:b9:67:9a:8f:39:0b:83:09:ae:50:98:69:13:85:ad:3b:47:c6:47:e0:ec:f2:46:87:ca:83:83:79:fc:1b:de:10:81:83:d4:48:0b:70:82:c5:a9:38:23:9f:6c:04:5b:f4:e6:78:9e:af:2d:24:17:a4:bd:e9:45:7d:81:52:e2:7f:45:d2:2f:b2:ea:d2:a6:4f:a3:e6:59:4b:17:7d:75:6a:04:b1:fe:1c:31:22:a7:0e:07:3b:42:e6:d1:44:ea:dc:62:c4:68:23:83:0c:37:07:15:61:a2:25:8b:af:5c:fe:45:dd:5d:e7:25:db:e9:fb:f6:57:7a:66:71:c0:1b:bd:45:d0:4e:4e:5c:f2:ae:aa:6f:e7:a2:34:c5:5a:6a:19:ff:d0:de:eb:b7:db:58:80:16:fe:07:7a:c2:f1:43:4c:dc:57:4b:d7:a1:9c:66:b9:66:1c:03:7e:9d:81:f8:d6:a6:36:8b:5b:03:f4:a1:48:5e:fd:7b:99:d8:c3:69:99:93:68:0f:7e:61:2f:19:b9:e8:c2:e4:65:1f:fa:57:ff:8f:85:7e:dd:da:a4:df:5e:63:77:50:2a:64:ad:d2:66:5f:35:67:21:ff:07:1e:23:50:5d:0c:48:9f:89:c5:63:93:05:59:71:81:90:79:cd:0b:47:ec:4d:15:6b:df:dd:6a:7a:45:62:16:07:0d:4c:3d:f0:95:5b:01:d5:65:d4:29:a9:78:a1:ad:82:43:30:10:60:f2:07:08:9c:91:f3:ea:81:fa:cf:14:71:ae:eb:de:c4:8e:40:7c:ee:48:97:5a:c3:86:cf:a1:b7:f3:d8:30:50:4d:03:97:b5:30:de:91:44:69:13:77:57:90:11:d5:97:7f:a6:55:7e:19:e6:88:d9:c4:4f:8a:34:5d:53:90:aa:c8:40:23:9a:2f:73:b7:34:f5:af:5e:69:d0:c9:d6:40:b3:80:74:b9:c5:74:8a:4f:d4:18:d9:72:01:d8:ba:86:bb:39:f0:7b:f6:25:81:8b:54:a2:89:84:50:ed:55:6e:ae:75:e2:b7:f5:f2:ab:70:8d:07:d4:0f:8e:4e:25:83:39:27:c4:87:ac:a6:ad:02:1b:e2:16:b1:06:63:0c:0f:dc:b3:6c:d7:9f:29:78:e9:3a:d9:1d:1a:93:77:7d:b6:07:d6:3c:03:9c:16:e4:6e:11:30:38:d4:ea:a4:d5:8e:fd:ad:52:e4:19:3f:91:b1:bb:8e:51:fd:ca:d2:71:c5:fa:ab:f0:8b:44:fd:c5:be:dd:fb:b4:16:5a:e5:48:6f:82:a1:31:74:d8:43:b8:99:a3:da:40:85:7a:a0:38:82:dc:73:06:a5:53:7c:a4:51:df:ea:a1:27:a1:8c:f3:46:30:60:7d:54:09:af:7f:7b:09:90:17:79:0c:0a:d7:29:43:e3:00:1d:0f:71:70:a2:c0:b0:93:46:0f:5b:c1:5b:c7:76:a7:bd:1b:d6:82:0a:a4:cf:c6:f7:0b:19:19:1c:0c:21:df:cd:cd:b8:bf:6a:94:bf:80:28:03:94:a0:75:bc:83:82:1d:97:c8:7d:a7:ea:c0:f7:e4:f6:a3:c0:ba:ad:0b:c6:44:68:44:fe:cf:aa:2a:7d:e0:73:23:89:a3:5a:6b:ca:40:bd:8f:05:cc:1d:67:67:72:0f:83:28:4f:39:6f:4f:0a:72:2b:3e:43:5a:eb:b3:18:ba:c1:1f:fe:26:f9:46:ba:ec:a2:63:fa:fb:22:d4:c7:15:29:3f:8a:82:ea:a2:d9:b0:19:af:02:6d:c2:d0:78:bf:31:8e:80:1d:2c:34:ec:40:60:b9:3b:08:f7:e6:23:ae:dd:70:00:7c:0c:0f:e8:7f:91:30:8f:42:9d:c1:4d:08:22:97:b1:86:a5:84:9a:9a:df:c0:e3:82:ef:26:91:fb:17:5b:3d:b3:4c:73:e6:26:c7:54:d1:23:d1:fc:80:5e:af:f9:a5:e2:09:e6:9a:2e:b8:52:86:1a:d9:0a:3b:7c:77:d7:83:76:6e:e1:54:64:fc:da:98:7c:a2:1f:8a:39:a5:18:ea:20:71:9a:90:43:9f:19:e8:69:5c:08:a9:70:a4:62:74:e2:21:f8:9c:01:69:48:9a:b5:4c:18:2e:df:ca:1f:8c:9e:b7:c1:6a:e2:a4:d2:8f:3b:f1:cb:25:64:6f:37:31:db:9b:0c:5d:70:cd:42:15:0c:c8:37:78:92:19:4b:18:ec:b1:43:82:68:19:76:e3:fd'
ip_src = '192.168.2.182'
timestamp = 1563843257911
msg_type = 14

es = Elasticsearch('192.168.2.140:9200')
s = Search(using=es, index="cipher-*")
s = s[0:10000]
if msg_type == 12:
    q = Q('match', layers__kerberos_msg_type=11) & Q('match',layers__ip_dst=ip_src) & Q('match', layers__kerberos_cipher__keyword=cipher)

if msg_type == 14:
    q = (Q('match', layers__kerberos_msg_type=11) | Q('match', layers__kerberos_msg_type=13)) & Q('match',layers__ip_dst=ip_src) & Q('match', layers__kerberos_cipher__keyword=cipher)
s1 = s.query(q)
response = s1.execute()
if len(response) != 0:
    print('normal')

else:
    qtime = Q('range', timestamp={'gte': int(timestamp), 'lte': int(timestamp) + 1000}) & Q('match', layers__ip_dst = ip_src) & Q('match', layers__kerberos_error_code = 32)
    s2 = s.query(qtime)
    response2 = s2.execute()
    if len(response2) == 0:
        if msg_type == 12:
            qsilver = Q('match', layers__kerberos_cipher__keyword=cipher)
            s3 = s.query(qsilver)
            response3 = s3.execute()
            for h in response3:
                id = h.meta.id
                index = h.meta.index
            if len(response3) != 0:
                es.update(index=index, doc_type='doc', id=id, body={'doc': {'indicator': 'attack: Golden Ticket is used'}})
            print('Golden ticket was used on ' + str(ip_src))
        if msg_type == 14:
            qsilver = Q('match', layers__kerberos_cipher__keyword=cipher)
            s3 = s.query(qsilver)
            response3 = s3.execute()
            for h in response3:
                id = h.meta.id
                index = h.meta.index
            if len(response3) != 0:
                es.update(index=index, doc_type='doc', id=id, body={'doc': {'indicator': 'attack: Silver Ticket is used'}})
            print('Silver ticket was used on ' + str(ip_src))
    else:
        print('normal')