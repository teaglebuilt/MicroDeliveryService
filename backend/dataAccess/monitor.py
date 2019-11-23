import json
import requests
import sys

auth = ('guest', 'guest')
url = 'http://localhost:15672/api/queues'

try:
    r = requests.get(url, auth=auth)
except:
    print ("target unavailable: {}".format(url))
    sys.exit()

queues_info = json.loads(r.text)

for queue in queues_info:
    print("queue: {}".format(queue.get('name', 'unavailable')))
    print("state: {}".format(queue.get('state', 'unavailable')))
    print("consumers: {}".format(queue.get('consumers', 'unavailable')))

    if "message_stats" not in queue:
        print ("no message_status\n")
        continue

    stats = queue["message_stats"]
    print("messages: [ack: {}, deliver: {}, publish: {}]".format(stats.get('ack'), stats.get('deliver'), stats.get('publish')))
    print()