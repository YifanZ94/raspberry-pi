from gpiozero import LED
import time

#%%   GPIO setup
enable = LED(17)
direc = LED(23)
step = LED(24)
MS1 = LED(5)
MS2 = LED(6)

#%%
class motor:
    def __init__(self):
        self.enable = enable
        self.direc = direc
        self.step = step
        self.MS1 = MS1
        self.MS2 = MS2
        
        self.stepdelay = 0.001
        self.MS1.off()
        self.MS2.on()
        
    def move(self,steps,direc): 
        if direc == 0:
            self.direc.on()
        else:
            self.direc.off()
        self.enable.off()
        
        for i in range(steps):
            self.step.on()
            time.sleep(self.stepdelay)
            step.off()
            time.sleep(self.stepdelay)
            
        self.enable.on()

#%%  test settings

