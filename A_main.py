# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:51:18 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from MotorDriver import motor
from MMC5603 import Mag
from KNNscikitlearn import KNN
from ssd_class import SSD
import time

Motor = motor()
sensor = Mag()
algorithm = KNN()
ssd = SSD()
## setting
dis_total = 30
dis_increment = 0.5
steps = round(dis_increment*3*250/5.3)
data_points = int(dis_total/dis_increment)

#%%  start measuring
direc = 1
warmup = sensor.all_data()
env = np.load('env.npy')
data = []
location = []

for i in range(data_points):
    Motor.move(steps,direc)
    time.sleep(0.1)
    reading = sensor.all_data() - env[i]
    loc = algorithm.search(reading)
    data.append(reading)
    location.append(loc)
    disp_loc = round(loc[0][0][0],2)
    ssd.display(disp_loc)
    time.sleep(0.5)
    
#%%     return
direc = 0
Motor.move(steps*data_points,direc)

#%% plot
x = np.arange(len(data))
npData = np.array(data)
y = npData[:,2]
plt.plot(x,y)
plt.show()

#%%  save the data
filename = input('enter the file name ')
file = open(filename + '.txt', 'w')
np.savetxt(file, np.array(data))
file.close()