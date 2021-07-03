""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
from datetime import datetime
from time import sleep 

def main(): 
    path = '/data.txt'
    data_file = open(path,'a')
    denom = ","
    print('starting...') 
    while True: 
        try: 
            
            RH = 50
            T = 28

            print('Temp: ', T , 'Hum: ', RH)
            sleep(2) 
        except: 
            data_file.close()
            print('exiting.') 
            break 
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
        print(dat)

        data_file.write(str(dat))
# call main 
if __name__ == '__main__': 
   main()  
