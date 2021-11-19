import paho.mqtt.client as mqtt
import os.path

certificates_path = "/Users/gaston/certificates" #你的存檔路徑
ca_certificate = os.path.join(certificates_path, "ca.crt") #os.path.join() 將多個路徑組合後返回
client_certificate = os.path.join(certificates_path, "device001.crt")


mqtt_server_host = "localhost" #mqtt server ip address
mqtt_server_port = 8883
mqtt_keepalive = 60 #numbers of seconds

#callback function
#on_connect: 當mqtt client接收到mqtt server的CONNACK回應時，也就是成功建立連線
def on_connect(client, userdata, rc):
    print("Connect result: {}".format(mqtt.connack_string(rc)))
    client.subscribe("test/drone01")
    
    
    def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed with QoS: {}".format(granted_qos[0]))

def on_message(client, userdata, msg):
    payload_string = msg.payload.decode('utf-8')
    print("Topic: {}. Payload: {}".format(
        msg.topic, 
        str(msg.payload)payload_string))
