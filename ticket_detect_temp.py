import os, time, pickle, json
import pandas as pd
from flask import Flask, request

golden_df_log='golden_df_logs.pickle'
silver_df_log='silver_df_logs.pickle'

cols = ['timestamp', 'ip_dst', 'ip_src', 'kerberos_CNameString', 'kerberos_cipher', 'kerberos_msg_type']

print('init called')
if os.path.exists(golden_df_log)==True:
    with open(golden_df_log, mode='rb') as f:
        golden_df=pickle.load(f)
else:
    golden_df = pd.DataFrame(index=[], columns=cols)

if os.path.exists(silver_df_log)==True:
    with open(silver_df_log, mode='rb') as f:
        silver_df=pickle.load(f)
else:
    silver_df = pd.DataFrame(index=[], columns=cols)
    print(silver_df.head())

app = Flask(__name__)
@app.route('/cipher', methods=['POST'])
def cipher():
    global golden_df, silver_df

    message = request.form.get('message', None)
    message = message.strip("'")

    try:
        message = json.loads(message)
    except:
        with open('parse_error.log', 'a') as f:
            print(message, file=f)
        return 'parse_error'

    if int(message['layers']['kerberos_msg_type'][0]) == 11:
        golden_df_timestamp = pd.DataFrame([message['timestamp']], columns=['timestamp'])
        golden_df_data = pd.DataFrame.from_dict(message['layers'])
        golden_df_line = pd.concat([golden_df_timestamp, golden_df_data], axis=1)
        golden_df = pd.concat([golden_df, golden_df_line])

    elif int(message['layers']['kerberos_msg_type'][0]) == 12:
        time.sleep(0.5)
        cipher = message['layers']['kerberos_cipher'][0]
        ip_src = message['layers']['ip_src'][0]
        account = message['layers']['kerberos_CNameString'][0]
        result = golden_df[golden_df.ip_dst.str.contains(ip_src)&golden_df.kerberos_CNameString.str.contains(account)&golden_df.kerberos_cipher.str.contains(cipher)]
        if len(result) == 0:
            print('attack')
            return 'attack'

    elif int(message['layers']['kerberos_msg_type'][0]) == 13:
        silver_df_timestamp = pd.DataFrame([message['timestamp']], columns=['timestamp'])
        silver_df_data = pd.DataFrame.from_dict(message['layers'])
        silver_df_line = pd.concat([silver_df_timestamp, silver_df_data], axis=1)
        silver_df = pd.concat([silver_df, silver_df_line])

    elif int(message['layers']['kerberos_msg_type'][0]) == 14:
        time.sleep(0.5)
        cipher = message['layers']['kerberos_cipher'][0]
        ip_src = message['layers']['ip_src'][0]
        account = message['layers']['kerberos_CNameString'][0]
        result_golden = golden_df[golden_df.ip_dst.str.contains(ip_src)&golden_df.kerberos_CNameString.str.contains(account)&golden_df.kerberos_cipher.str.contains(cipher)]
        result_silver = silver_df[silver_df.ip_dst.str.contains(ip_src)&silver_df.kerberos_CNameString.str.contains(account)&silver_df.kerberos_cipher.str.contains(cipher)]
        result = result_golden + result_silver
        if len(result) == 0:
            print('attack')
            return 'attack'

    print('normal')
    return 'normal'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', threaded=True)
    finally:
        print('finally called')
        with open(golden_df_log, mode='wb') as handle:
            pickle.dump(golden_df, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(silver_df_log, mode='wb') as handle:
            pickle.dump(silver_df, handle, protocol=pickle.HIGHEST_PROTOCOL)