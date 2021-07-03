""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
import RPi.GPIO as GPIO 
from datetime import datetime
from time import sleep 
import Adafruit_DHT 

def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23) 
   return (str(RH), str(T)) 
def main(): 
    path = '/data.txt'
    data_file = open(path,'w')
    print('starting...') 
    while True: 
        try: 
            dateTimeObj = datetime.now()
            print('y: ', dateTimeObj.year, 'm: ', dateTimeObj.month, 'd: ', dateTimeObj.day)
            print('H: ', dateTimeObj.hour, 'Min :', dateTimeObj.minute)
            RH, T = getSensorData() 
            data_file.write(dateTimeObj.year,',',dateTimeObj.month,',',dateTimeObj.day,',',dateTimeObj.hour,',',dateTimeObj.minute,',',T,',',RH)
            print('Temp: ', T , 'Hum: ', RH)
            sleep(2) 
        except: 
            data_file.close()
            print('exiting.') 
            break 
# call main 
if __name__ == '__main__': 
   main()  
