#ca.crt: Certificate authority certificate file
#device001.crt: Client certificate file
#device001.key: Client key

import paho.mqtt.client as mqtt
import os.path

certificates_path = "/Users/gaston/certificates" #你的存檔路徑
ca_certificate = os.path.join(certificates_path, "ca.crt") #os.path.join() 將多個路徑組合後返回
client_certificate = os.path.join(certificates_path, "device001.crt")


mqtt_server_host = "localhost" #mqtt server ip address
mqtt_server_port = 8883 #連接埠1883 與8883 (TLS 加密連線)
mqtt_keepalive = 60 #numbers of seconds

#callback function
#on_connect: 當mqtt client接收到mqtt server的CONNACK回應時，也就是成功建立連線時，則執行function    
def on_connect(client, userdata, rc):
    print("Connect result: {}".format(mqtt.connack_string(rc)))
    client.subscribe("test/drone01")
    
#on_subscribe: 當mqtt client接收到mqtt server的SUBACK回應時，也就是訂閱完成時，則執行function     
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed with QoS: {}".format(granted_qos[0]))
    
#on_message: 當mqtt client接收到mqtt server的PUBLISH訊息時，每當mqtt server發布訊息，基於client的訂閱，則執行function
def on_message(client, userdata, msg):
    payload_string = msg.payload.decode('utf-8')
    print("Topic: {}. Payload: {}".format(
        msg.topic, 
        str(msg.payload)payload_string))
    
if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    #如果使用1883，而非8883，則不需此行
    #client.tls_set(ca_certs = ca_certificate, certfile=client_certificate, keyfile=client_key)
    client.connect_async(host=mqtt_server_host, port=mqtt_server_port, keepalive=mqtt_keepalive) 
    client.loop_forever()
