#https://www.rocksaying.tw/archives/2016/MQTT-3-Python-clients.html

import paho.mqtt.publish as publish

# publish a message then disconnect.
host = "your_broker_ip"
topic = "your_topic"
payload = "message_you_publish"

# If broker asks user/password.
auth = {'username': "", 'password': ""}

# If broker asks client ID.
client_id = ""

publish.single(topic, payload, qos=1, hostname=host)
#publish.single(topic, payload, qos=1, host=host, auth=auth, client_id=client_id)
