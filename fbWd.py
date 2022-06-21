def main():
    # This program will let you test your ESC and brushless motor.
    # Make sure your battery is not connected if you are going to calibrate it at first.
    # Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
    # This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful
    # pssst Its not, its safe   
    import main   #importing logging python script to write data from propellers to log file
    import os     #importing os library so as to communicate with the system
    import time   #importing time library to make Rpi wait because its too impatient 
    os.system("sudo pigpiod") #Launching GPIO library
    time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
    import pigpio #importing GPIO library
    
    ESC1=4
    ESC2=2 
    ESC3=3 
    ESC4=14
    ESCL=15
    ESCR=18

    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC1, 0) 
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0) 
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.set_servo_pulsewidth(ESCL, 0) 
    pi.set_servo_pulsewidth(ESCR, 0)


    max_value =  2000 #change this if your ESC's max value is different or leave it be
    min_value = 1000  #change this if your ESC's min value is different or leave it be
    print("For first time launch, select calibrate")
    print("Type the exact word for the function you want")
    print("calibrate OR manual OR control OR arm OR stop")

    def manual_drive(): #You will use this function to program your ESC if required
        print("You have selected manual option so give a value between 0 and you max value")    
        while True:
            inp = input()
            if inp == "stop":
                stop()
                break
            elif inp == "control":
                control()
                break
            elif inp == "arm":
                arm()
                break
            else:
                pi.set_servo_pulsewidth(ESC1,inp)
                pi.set_servo_pulsewidth(ESC2,inp)
                pi.set_servo_pulsewidth(ESC3,inp)
                pi.set_servo_pulsewidth(ESC4,inp)
                pi.set_servo_pulsewidth(ESCL,inp)
                pi.set_servo_pulsewidth(ESCR,inp)

                    
    def calibrate():   #This is the auto calibration procedure of a normal ESC
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        pi.set_servo_pulsewidth(ESC4, 0)
        pi.set_servo_pulsewidth(ESCL, 0)
        pi.set_servo_pulsewidth(ESCR, 0)
        print("Disconnect the battery and press Enter")
        inp = input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC1, max_value)
            pi.set_servo_pulsewidth(ESC2, max_value)
            pi.set_servo_pulsewidth(ESC3, max_value)
            pi.set_servo_pulsewidth(ESC4, max_value)
            pi.set_servo_pulsewidth(ESCL, max_value)
            pi.set_servo_pulsewidth(ESCR, max_value)
            print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
            inp = input()
            if inp == '':            
                pi.set_servo_pulsewidth(ESC1, min_value)
                pi.set_servo_pulsewidth(ESC2, min_value)
                pi.set_servo_pulsewidth(ESC3, min_value)
                pi.set_servo_pulsewidth(ESC4, min_value)
                pi.set_servo_pulsewidth(ESCL, min_value)
                pi.set_servo_pulsewidth(ESCR, min_value)
                print("Wierd eh! Special tone")
                time.sleep(7)
                print("Wait for it ....")
                time.sleep (5)


                
                print("Im working on it, DONT WORRY JUST WAIT.....")
                pi.set_servo_pulsewidth(ESC1, 0)
                pi.set_servo_pulsewidth(ESC2, 0)
                pi.set_servo_pulsewidth(ESC3, 0)
                pi.set_servo_pulsewidth(ESC4, 0)
                pi.set_servo_pulsewidth(ESCL, 0)
                pi.set_servo_pulsewidth(ESCR, 0)

                time.sleep(2)
                print("Arming ESC now...")
                pi.set_servo_pulsewidth(ESC1, min_value)
                pi.set_servo_pulsewidth(ESC2, min_value)
                pi.set_servo_pulsewidth(ESC3, min_value)
                pi.set_servo_pulsewidth(ESC4, min_value)
                pi.set_servo_pulsewidth(ESCL, min_value)
                pi.set_servo_pulsewidth(ESCR, min_value)
                time.sleep(1)
                print("See.... uhhhhh")
                control() # You can change this to any other function you want

    def fWd():
        CwSpeed = 1500 #3, 4 ters bağlantılı. Bundan dolayı ayrı hız değişkeni kulllanıldı. 
        aCwSpeed = 1500 #CwSpeed 1 ve 2, aCwSpeed 3 ve  için.
        counter = 0
        loop = True
        while loop == True: #ana döngü 
            while counter <= 5: #motorların hızını kademeli artırmak için döngü
                pi.set_servo_pulsewidth(ESC1, CwSpeed)
                pi.set_servo_pulsewidth(ESC2, CwSpeed)
                pi.set_servo_pulsewidth(ESC3, aCwSpeed)
                pi.set_servo_pulsewidth(ESC4, aCwSpeed)
                CwSpeed += 100 #motor hızında kullanılan CwSpeed ve aCwSpeed değişkenlerinin değeri artar.
                aCwSpeed -= 100 
                counter += 1
                time.sleep(0.5) #hız artırma döngüsünün gecikmesi için saniye cinsinden bekleme
            time.sleep(5) #motorlar tam güç 5 saniye boyunca çalışır. 
            stop()#ana döngü bitirilir.
            loop = False


    def control(): 
        loop = True
        print("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
        time.sleep(1)
        speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
        print("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed. Press x to stop.")
        while loop == True:
            pi.set_servo_pulsewidth(ESC1, speed)
            pi.set_servo_pulsewidth(ESC2, speed)
            pi.set_servo_pulsewidth(ESC3, speed)
            pi.set_servo_pulsewidth(ESC4, speed)
            pi.set_servo_pulsewidth(ESCL, speed)
            pi.set_servo_pulsewidth(ESCR, speed)
            

            inp = input()
            if inp == "x":
                loop = False
            elif inp == "q":
                speed -= 100    # decrementing the speed like hell
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "e":    
                speed += 100    # incrementing the speed like hell
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "d":
                speed += 10     # incrementing the speed 
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "a":
                speed -= 10     # decrementing the speed
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "stop":
                stop()          #going for the stop function
                break
            elif inp == "manual":
                manual_drive()
                break

            elif inp == "arm":
           # This program will let you test your ESC and brushless motor.
    # Make sure your battery is not connected if you are going to calibrate it at first.
    # Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
    # This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful
    # pssst Its not, its safe   
    import main   #importing logging python script to write data from propellers to log file
    import os     #importing os library so as to communicate with the system
    import time   #importing time library to make Rpi wait because its too impatient 
    os.system("sudo pigpiod") #Launching GPIO library
    time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
    import pigpio #importing GPIO library
    
    ESC1=4
    ESC2=2 
    ESC3=3 
    ESC4=14
    ESCL=15
    ESCR=18

    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC1, 0) 
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0) 
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.set_servo_pulsewidth(ESCL, 0) 
    pi.set_servo_pulsewidth(ESCR, 0)


    max_value =  2000 #change this if your ESC's max value is different or leave it be
    min_value = 1000  #change this if your ESC's min value is different or leave it be
    print("For first time launch, select calibrate")
    print("Type the exact word for the function you want")
    print("calibrate OR manual OR control OR arm OR stop")

    def manual_drive(): #You will use this function to program your ESC if required
        print("You have selected manual option so give a value between 0 and you max value")    
        while True:
            inp = input()
            if inp == "stop":
                stop()
                break
            elif inp == "control":
                control()
                break
            elif inp == "arm":
                arm()
                break
            else:
                pi.set_servo_pulsewidth(ESC1,inp)
                pi.set_servo_pulsewidth(ESC2,inp)
                pi.set_servo_pulsewidth(ESC3,inp)
                pi.set_servo_pulsewidth(ESC4,inp)
                pi.set_servo_pulsewidth(ESCL,inp)
                pi.set_servo_pulsewidth(ESCR,inp)

      #donda              
    def calibrate():   #This is the auto calibration procedure of a normal ESC
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        pi.set_servo_pulsewidth(ESC4, 0)
        pi.set_servo_pulsewidth(ESCL, 0)
        pi.set_servo_pulsewidth(ESCR, 0)
        print("Disconnect the battery and press Enter")
        inp = input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC1, max_value)
            pi.set_servo_pulsewidth(ESC2, max_value)
            pi.set_servo_pulsewidth(ESC3, max_value)
            pi.set_servo_pulsewidth(ESC4, max_value)
            pi.set_servo_pulsewidth(ESCL, max_value)
            pi.set_servo_pulsewidth(ESCR, max_value)
            print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
            inp = input()
            if inp == '':            
                pi.set_servo_pulsewidth(ESC1, min_value)
                pi.set_servo_pulsewidth(ESC2, min_value)
                pi.set_servo_pulsewidth(ESC3, min_value)
                pi.set_servo_pulsewidth(ESC4, min_value)
                pi.set_servo_pulsewidth(ESCL, min_value)
                pi.set_servo_pulsewidth(ESCR, min_value)
                print("Wierd eh! Special tone")
                time.sleep(7)
                print("Wait for it ....")
                time.sleep (5)


                
                print("Im working on it, DONT WORRY JUST WAIT.....")
                pi.set_servo_pulsewidth(ESC1, 0)
                pi.set_servo_pulsewidth(ESC2, 0)
                pi.set_servo_pulsewidth(ESC3, 0)
                pi.set_servo_pulsewidth(ESC4, 0)
                pi.set_servo_pulsewidth(ESCL, 0)
                pi.set_servo_pulsewidth(ESCR, 0)

                time.sleep(2)
                print("Arming ESC now...")
                pi.set_servo_pulsewidth(ESC1, min_value)
                pi.set_servo_pulsewidth(ESC2, min_value)
                pi.set_servo_pulsewidth(ESC3, min_value)
                pi.set_servo_pulsewidth(ESC4, min_value)
                pi.set_servo_pulsewidth(ESCL, min_value)
                pi.set_servo_pulsewidth(ESCR, min_value)
                time.sleep(1)
                print("See.... uhhhhh")
                control() # You can change this to any other function you want

    def fWd():
        CwSpeed = 1500 #3, 4 ters bağlantılı. Bundan dolayı ayrı hız değişkeni kulllanıldı. 
        aCwSpeed = 1500 #CwSpeed 1 ve 2, aCwSpeed 3 ve  için.
        counter = 0
        loop = True
        while loop == True: #ana döngü 
            while counter <= 5: #motorların hızını kademeli artırmak için döngü
                pi.set_servo_pulsewidth(ESC1, CwSpeed)
                pi.set_servo_pulsewidth(ESC2, CwSpeed)
                pi.set_servo_pulsewidth(ESC3, aCwSpeed)
                pi.set_servo_pulsewidth(ESC4, aCwSpeed)
                CwSpeed += 100 #motor hızında kullanılan CwSpeed ve aCwSpeed değişkenlerinin değeri artar.
                aCwSpeed -= 100 
                counter += 1
                time.sleep(0.5) #hız artırma döngüsünün gecikmesi için saniye cinsinden bekleme
            time.sleep(5) #motorlar tam güç 5 saniye boyunca çalışır. 
            stop()#ana döngü bitirilir.
            loop = False


    def control(): 
        loop = True
        print("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
        time.sleep(1)
        speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
        print("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed. Press x to stop.")
        while loop == True:
            pi.set_servo_pulsewidth(ESC1, speed)
            pi.set_servo_pulsewidth(ESC2, speed)
            pi.set_servo_pulsewidth(ESC3, speed)
            pi.set_servo_pulsewidth(ESC4, speed)
            pi.set_servo_pulsewidth(ESCL, speed)
            pi.set_servo_pulsewidth(ESCR, speed)
            

            inp = input()
            if inp == "x":
                loop = False
            elif inp == "q":
                speed -= 100    # decrementing the speed like hell
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "e":    
                speed += 100    # incrementing the speed like hell
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "d":
                speed += 10     # incrementing the speed 
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "a":
                speed -= 10     # decrementing the speed
                main.wrtLg(1, "speed = %d" % speed)
                print("speed = %d" % speed)
            elif inp == "stop":
                stop()          #going for the stop function
                break
            elif inp == "manual":
                manual_drive()
                break

            elif inp == "arm":
                arm()
                break    
            else:
                print("WHAT DID I SAID!! Press a,q,d or e")
                
    def arm(): #This is the arming procedure of an ESC 
        print("Connect the battery and press Enter")
        inp = input()    
        if inp == '':
            pi.set_servo_pulsewidth(ESC1, 0)
            pi.set_servo_pulsewidth(ESC2, 0)
            pi.set_servo_pulsewidth(ESC3, 0)
            pi.set_servo_pulsewidth(ESC4, 0)
            pi.set_servo_pulsewidth(ESCL, 0)
            pi.set_servo_pulsewidth(ESCR, 0)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC1, max_value)
            pi.set_servo_pulsewidth(ESC2, max_value)
            pi.set_servo_pulsewidth(ESC3, max_value)
            pi.set_servo_pulsewidth(ESC4, max_value)
            pi.set_servo_pulsewidth(ESCL, max_value)
            pi.set_servo_pulsewidth(ESCR, max_value)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
            pi.set_servo_pulsewidth(ESCL, min_value)
            pi.set_servo_pulsewidth(ESCR, min_value)
            time.sleep(1)
            fWd()
            
    def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        pi.set_servo_pulsewidth(ESC4, 0)
        pi.set_servo_pulsewidth(ESCL, 0)
        pi.set_servo_pulsewidth(ESCR, 0)
        pi.stop()

    #This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.    
    inp = input()
    if inp == "manual":
        manual_drive()
    elif inp == "calibrate":
        calibrate()
    elif inp == "arm":
        arm()
    elif inp == "control":
        control()
    elif inp == "stop":
        stop()

    else :
        print("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")

         arm()
                break    
            else:
                print("WHAT DID I SAID!! Press a,q,d or e")
                
    def arm(): #This is the arming procedure of an ESC 
        print("Connect the battery and press Enter")
        inp = input()    
        if inp == '':
            pi.set_servo_pulsewidth(ESC1, 0)
            pi.set_servo_pulsewidth(ESC2, 0)
            pi.set_servo_pulsewidth(ESC3, 0)
            pi.set_servo_pulsewidth(ESC4, 0)
            pi.set_servo_pulsewidth(ESCL, 0)
            pi.set_servo_pulsewidth(ESCR, 0)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC1, max_value)
            pi.set_servo_pulsewidth(ESC2, max_value)
            pi.set_servo_pulsewidth(ESC3, max_value)
            pi.set_servo_pulsewidth(ESC4, max_value)
            pi.set_servo_pulsewidth(ESCL, max_value)
            pi.set_servo_pulsewidth(ESCR, max_value)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
            pi.set_servo_pulsewidth(ESCL, min_value)
            pi.set_servo_pulsewidth(ESCR, min_value)
            time.sleep(1)
            fWd()
            
    def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        pi.set_servo_pulsewidth(ESC4, 0)
        pi.set_servo_pulsewidth(ESCL, 0)
        pi.set_servo_pulsewidth(ESCR, 0)
        pi.stop()

    #This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.    
    inp = input()
    if inp == "manual":
        manual_drive()
    elif inp == "calibrate":
        calibrate()
    elif inp == "arm":
        arm()
    elif inp == "control":
        control()
    elif inp == "stop":
        stop()

    else :
        print("Thank You for not following the things I'm saying... now you gotta restart the program ALLAHSIZ !!")
if _name_ == "_main_":
    main()
    #lean-code
