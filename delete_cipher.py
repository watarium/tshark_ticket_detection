import schedule, time
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

def deletecipher():
    now = datetime.now()
    now = float(now.timestamp()*1000)
    pasteleven = now - 39600000
    print(now)
    print(pasteleven)

    es = Elasticsearch('192.168.2.140:9200')
    s = Search(using=es, index="cipher")
    s = s[0:10000]

    qtime = Q('range', timestamp={'lte': int(pasteleven)})
    s = s.query(qtime)
    response = s.execute()

    for h in response:
        id = h.meta.id
        index = h.meta.index
        es.delete(index=index, doc_type='doc', id=id)
        print('deleted ' + str(id))

schedule.every().hour.do(deletecipher)

while True:
    schedule.run_pending()
    time.sleep(10)