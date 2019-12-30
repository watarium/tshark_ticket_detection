import os, pickle, json
import pandas as pd

f = open("tshark.json", 'r')
json_tshark = json.load(f)

golden_df_log='golden_df_logs.pickle'
silver_df_log='silver_df_logs.pickle'

print('init called')
if os.path.exists(golden_df_log)==True:
    with open(golden_df_log, mode='rb') as f:
        golden_df=pickle.load(f)
else:
    golden_df = pd.DataFrame()

if os.path.exists(silver_df_log)==True:
    with open(silver_df_log, mode='rb') as f:
        silver_df=pickle.load(f)
else:
    silver_df = pd.DataFrame()

message = json_tshark

def detect_ticket():
    if int(message['layers']['kerberos_msg_type'][0]) == 11:
        golden_df_timestamp = pd.DataFrame([message['timestamp']], columns=['timestamp'])
        golden_df_data = pd.DataFrame.from_dict(message['layers'])
        golden_df_line = pd.concat([golden_df_timestamp, golden_df_data], axis=1)
        golden_df = pd.concat([golden_df, golden_df_line])
        with open(golden_df_log, mode='wb') as handle:
            pickle.dump(golden_df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    elif int(message['layers']['kerberos_msg_type'][0]) == 12:
        cipher = message['layers']['kerberos_cipher'][0]
        if 'kerberos_cipher' in golden_df.columns:
            result = golden_df[golden_df.kerberos_cipher.str.contains(cipher)]
            if len(result) == 0:
                print('attack')
                return 'attack'

    elif int(message['layers']['kerberos_msg_type'][0]) == 13:
        silver_df_timestamp = pd.DataFrame([message['timestamp']], columns=['timestamp'])
        silver_df_data = pd.DataFrame.from_dict(message['layers'])
        silver_df_line = pd.concat([silver_df_timestamp, silver_df_data], axis=1)
        silver_df = pd.concat([silver_df, silver_df_line])
        with open(silver_df_log, mode='wb') as handle:
            pickle.dump(silver_df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    elif int(message['layers']['kerberos_msg_type'][0]) == 14:
        cipher = message['layers']['kerberos_cipher'][0]
        if 'kerberos_cipher' in silver_df.columns:
            result = silver_df[silver_df.kerberos_cipher.str.contains(cipher)]
            if len(result) == 0:
                print('attack')
                return 'attack'

    print('normal')
    return 'normal'

detect_ticket()