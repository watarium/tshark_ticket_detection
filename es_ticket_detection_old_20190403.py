import time, threading, json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from flask import Flask, request

def ticketcheck(ip_src, cipher, timestamp):

    time.sleep(1)

    es = Elasticsearch('192.168.2.140:9200')
    s = Search(using=es, index="cipher-*")
    s = s[0:10000]
    q = Q('match', layers__kerberos_msg_type= 13) & Q('match', layers__ip_dst = ip_src) & Q('match', layers__kerberos_cipher__keyword = cipher)
    s1 = s.query(q)
    response = s1.execute()
    if len(response) != 0:
        return 'normal'

    else:
        qtime = Q('range', timestamp={'gte': int(timestamp), 'lte': int(timestamp) + 1000}) & Q('match', layers__ip_dst = ip_src) & Q('match', layers__kerberos_error_code = 32)
        s2 = s.query(qtime)
        response2 = s2.execute()
        if len(response2) != 0:
            return 'normal'
        else:
            return 'Malicious ticket was used on ' + str(ip_src)

app = Flask(__name__)
@app.route('/tsharkmsg', methods=['POST'])
def tsharkmsg():

    message = request.form.get('message', None)
    message = message.strip("'")

    try:
        message = json.loads(message)
    except:
        with open('parse_error.log', 'a') as f:
            print(message, file=f)
        return 'parse_error'

    if int(message['layers']['kerberos_msg_type'][0]) == 14:
        ip_src = message['layers']['ip_src'][0]
        cipher = message['layers']['kerberos_cipher'][0]
        timestamp = message['timestamp']
        result = ticketcheck(ip_src, cipher, timestamp)
        return result
    else:
        return 'normal'

if __name__ == '__main__':
    app.run(host='0.0.0.0')