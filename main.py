import datetime

LGLVL = 1
#error 3
#warning 2
#all 1

#main
def wrtLg(lgLvl, msg):
    if lgLvl <= LGLVL:
        dtNw = datetime.datetime.now() 
        lgFl = open("/home/musdaa/monachus/log/log1.txt", "a")
        lgMsg =  str(dtNw.strftime("%Y-%m-%d %H:%M:%S")) + " - " + msg + "\n"
        lgFl.write(lgMsg)
        lgFl.close()

wrtLg(1, "Hello world!")
#initialise and configure propelers

#main infinite loop
    #read and parse port data#
    # send data to propeller
    # #send data to headlight
    # #send data to claw
# #end of infinite loop
