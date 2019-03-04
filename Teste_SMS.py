#..........................................................
#  ENVIA SMS - Testado com MiniMODEM VIVO 
#..........................................................
import time
import serial
 
print("Enviando SMS de teste ...")

ser = serial.Serial('/dev/ttyUSB3', 9600, timeout = 5)
ser.flushInput()

#..........................................................
#  ENVIA SMS
#..........................................................
ser.write('at\r'),                           time.sleep(2)
ser.write('at\r'),                           time.sleep(2)
ser.write('at\r'),                           time.sleep(2)    
ser.write('at+cnmi=1\r'),                    time.sleep(.5)    
ser.write('at+cmgf=1\r'),                    time.sleep(.5)
ser.write('at\r'),                           time.sleep(.5)
ser.write('at\r'),                           time.sleep(.5)
ser.write('at+cmgs="999755396"\r'),          time.sleep(.5)    
ser.write('MODEM VIVO\n')
ser.write('Agora...\n')
ser.write(time.strftime("%d/%m/%y") + '\n'), time.sleep(.5)
ser.write(time.strftime("%H:%M:%S") + '\n'), time.sleep(.5)  
ser.write(chr(26)),                          time.sleep(.5)
ser.write('at\r'),                           time.sleep(.5)
ser.write('at\r'),                           time.sleep(.5)
print(time.strftime("%d/%m/%y"))
print(time.strftime("%H:%M:%S"))
time.sleep(1)
ser.flushOutput()
#..........................................................

