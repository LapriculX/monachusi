import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC_TOP_LEFT=3
ESC1=3

pi = pigpio.pi()

pi.set_servo_pulsewidth(ESC_TOP_LEFT, 0) 

max_value = 2500 #change this if your ESC's max value is different or leave it be
min_value = 500  #change this if your ESC's min value is different or leave it be


def control(): 
    speed=int(input("what is the speed"))
    print(speed)
    pi.set_servo_pulsewidth(ESC_TOP_LEFT, speed) 

def calibrate(): 
    pi.set_servo_pulsewidth(ESC1, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC1, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC1, min_value)
            print("Wierd eh! Special tone")
            time.sleep(7)
            print("Wait for it ....")
            time.sleep (5)
            print("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC1, 0)
            time.sleep(2)
            print("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC1, min_value)
            time.sleep(1)
            print("See.... uhhhhh")
            control() # You can change this to any other function you want


        


inp=input()
if inp == "control":
    control()
elif inp=="calibrate":
    calibrate()


    
