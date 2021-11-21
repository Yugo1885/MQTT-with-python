import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Result Code:"+str(rc))
    client.subscribe("/home") #your topic

def on_message(client, userdata, msg):
    print(msg.topic+" "+ msg.payload.decode('utf-8'))

client = mqtt.Client() #初始化地端程式
client.on_connect = on_connect
client.on_message = on_message
client.connect("your_broker_ip", 1883, 60) #ip,port,連線時間

client.loop_forever() #開始連線
