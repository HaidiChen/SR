# broadcasting the result
import paho.mqtt.client as mqtt
import os
import requests
import time

OUTPUT_FOLDER = RD_FOLDER = '../rawdata/'

broker_url = '192.168.72.133'
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

while True:
    # part 1). grab the vehicle data from a single vehicle
    resp = requests.get('http://192.168.72.132:5000/expose')

    while resp.headers['filenumber'] != '0':
        fn = resp.headers['filename']

        with open(RD_FOLDER + fn, 'wb') as f:
            f.write(resp.content)

        resp = requests.get('http://192.168.72.132:5000/expose')


    # part 2). broadcast the data
    fileList = os.listdir(OUTPUT_FOLDER)

    while len(fileList):
        fname = fileList[0]
    
        with open(OUTPUT_FOLDER + fname, 'rb') as f:
            filepayload = f.read()
            filebyte = bytearray(filepayload)

            client.publish('filename', fname, 0, False)
            client.publish('result', filebyte, 0, False)

        os.remove(OUTPUT_FOLDER + fname)
        fileList = os.listdir(OUTPUT_FOLDER)

    time.sleep(30)