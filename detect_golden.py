from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

EVENT_ST="4769"
WARN="warning:ST without TGT"
#WARN="attack:test"
RESULT_NORMAL="normal"
DOC_TYPE="doc"

def update_realtime(ip_src):
    ip_ptn='*'+ip_src+'*'
    es = Elasticsearch('10.0.19.112:9200')
    s = Search(using=es, index='realtime-*')
    s = s[0:1]
    q = Q('match', indicator__keyword= WARN) & Q('match', event_id = EVENT_ST) & Q('match', event_data__IpAddress__keyword = ip_ptn)
    s1 = s.query(q)
    response = s1.execute()
    id=''
    index=''
    for h in response:
        id=h.meta.id
        index=h.meta.index
        #print(h.meta.id)

    if len(response) != 0:
        es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': 'attack: Golden Ticket is used'}})
        print('attack: Golden Ticket is used')
        return 'attack: Golden Ticket is used'

    else:
        RESULT_NORMAL


def update_packet(cipher):
    es = Elasticsearch('10.0.19.112:9200')
    s = Search(using=es, index='packet')
    s = s[0:1]
    q = Q('match', layers__kerberos_cipher = cipher)
    s1 = s.query(q)
    response = s1.execute()
    id=''
    index=''
    for h in response:
        id=h.meta.id
        index=h.meta.index
        kerberos_msg_type=h.layers.kerberos_msg_type[0]

    if len(response) != 0:
        if kerberos_msg_type==12:
            es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': 'attack: Golden Ticket is used'}})
            print('attack: Golden Ticket is used')
            return 'attack: Golden Ticket is used'
        if kerberos_msg_type==14:
            es.update(index=index, doc_type=DOC_TYPE, id=id, body={'doc': {'indicator': 'attack: Silver Ticket is used'}})
            print('attack: Silver Ticket is used')
            return 'attack: Silver Ticket is used'
    else:
        RESULT_NORMAL
