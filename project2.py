import time
import matplotlib.pyplot as plt
from drawnow import *
import serial
val = [ ]
count = 0
#create the serial port object
port = serial.Serial('COM12', 115200, timeout=0.5)#115200 is the standard baud rate
plt.ion()

#create the figure function
def makeFig():
    plt.ylim(-10,10)
    plt.title('Waveform Oscilloscope')
    plt.grid(True)
    plt.ylabel('Voltage(V)')
    plt.plot(val, 'b-', label='Channel 0')
    plt.legend(loc='lower right')

while (True):
    port.write(b'K') # ready signal to Arduino
    if (port.inWaiting()):# if the arduino replies
        value = port.readline()# read the reply
        print(value)#print value on terminal for monitoring
        number = (float(value)*5/1024)#scale data to corresponding value in V
        val.append(number)
        time.sleep(0.01)
        drawnow(makeFig)#update plot to reflect new data input
        plt.pause(0.01)
        count = count+1
    if(count>50):
        val.pop(0)#delete the element at position 0 to ensure that the space taken by the plot doesn't exceed 50 units on the z-axis. It also gives an illusion of movement of the wave due to persistence of vision
