import requests
import json
from collections import OrderedDict
url = 'https://api.datonis.io/api/v3/datonis_query/thing_data'

payload1 = '{"thing_key":"t1b48ta16b", "from":"2016/07/09 17:05:00", "to":"2016/07/10 17:00:00", "time_zone":"Mumbai","time_format":"str","per":"10"}'

#payload = json.loads(payload1, object_pairs_hook=OrderedDict)

headers = {'content-type': 'application/json', 'X-Access-Key' : '7tf589ff6tb86992bcdf8d9325ab39tf4be94348' }
r = requests.post(url, data=payload1, headers=headers)
print r.content







#curl -v -X POST -H "Content-Type:application/json" --header 'X-Access-Key:8t99cbb439bb98e719b5b14befa3d59tte9374tb' -d "{'thing_key':'t1b48ta16b', 'from':'2016/07/09 17:05:00', 'to':'2016/07/10 17:00:00', 'time_zone':'Mumbai' , 'time_format':'str', 'per':'10'}" 'https://api.datonis.io/api/v3/datonis_query/thing_data'
