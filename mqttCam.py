import paho.mqtt.client as mqtt
import cv2 
import time
#mqtt連線設定
broker = 'test.mosquitto.org'
port = 1883
topic = 'python/mqttCam'

#影像串流品質
width=320
height=240
quality=20

client = mqtt.Client()
client.connect(broker,port)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't open cam")
        break
    	
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 設定 JPEG 品質為 quality
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    # 編碼成jpeg 
    result,encoded = cv2.imencode('.jpg', gray, encode_param)
    # 發佈影像
    client.publish(topic, bytearray(encoded))
    cv2.imshow("image",gray)
    #time.sleep(0.5)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
client.release()
