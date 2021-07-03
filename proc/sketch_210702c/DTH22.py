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
    denom = ","
    print('starting...') 
    while True: 
        try: 
            RH, T = getSensorData()
            print('Temp: ', T , 'Hum: ', RH)
            
            dateTimeObj = datetime.now()
            print('y: ', dateTimeObj.year, 'm: ', dateTimeObj.month, 'd: ', dateTimeObj.day)
            print('H: ', dateTimeObj.hour, 'Min :', dateTimeObj.minute)
            year = dateTimeObj.year
            month = dateTimeObj.month
            day = dateTimeObj.day
            hour = dateTimeObj.hour
            minute = dateTimeObj.minute

            #dat = year , denom , month , denom , day , denom , hour , denom , minute , denom , T , denom , RH , '\n'
            dat = year , month , day , hour , minute , T , RH , '\n'
            print(str(dat))

            data_file.write(str(dat))

            sleep(2) 
        except: 
            data_file.close()
            print('exiting.') 
            break 
# call main 
if __name__ == '__main__': 
   main()  
