# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:24:52 2021

@author: Administrator
"""
import os
os.chdir('/home/pi/Desktop/A_system')

import numpy as np
from sklearn.neighbors import NearestNeighbors

B = np.load('BMap.npy')
LocMap = np.load('LocMap.npy')
NormP = np.load('NormParameter.npy')
#%%

class KNN:
    def __init__(self):
        self.neigh = NearestNeighbors(n_neighbors=1)
        self.neigh.fit(B)
        
    def search(self,measure):
        self.theta = 0.1067
        self.Normliezed = [(measure[0]-NormP[0][0])/NormP[0][3],
                           (measure[1]-NormP[0][1])/NormP[0][4],
                           (measure[2]-NormP[0][2])/NormP[0][5]]
        self.index = self.neigh.kneighbors([self.Normliezed], 1, return_distance=False)
        return  LocMap[self.index]
    