# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:50:15 2021

@author: Administrator
"""
import smbus

device = smbus.SMBus(1)
dev_addr = 0x30
identi_addr = 0x39

inter_control = 0x1b
X_H_add = 0x00
X_L_add = 0x01
Y_H_add = 0x02
Y_L_add = 0x03
Z_H_add = 0x04
Z_L_add = 0x05

class Mag:
    def __init__(self):
        self.device = device
        
    def all_data(self):
        self.device.write_byte_data(dev_addr,inter_control,0b00100001)
        self.X_L = self.device.read_byte_data(dev_addr,X_L_add)
        self.X_H = self.device.read_byte_data(dev_addr,X_H_add)
        self.Y_L = self.device.read_byte_data(dev_addr,Y_L_add)
        self.Y_H = self.device.read_byte_data(dev_addr,Y_H_add)
        self.Z_L = self.device.read_byte_data(dev_addr,Z_L_add)
        self.Z_H = self.device.read_byte_data(dev_addr,Z_H_add)
        self.Xbyte2long = self.X_H << 8 | self.X_L
        self.Ybyte2long = self.Y_H << 8 | self.Y_L
        self.Zbyte2long = self.Z_H << 8 | self.Z_L
        self.Xgauss = (self.Xbyte2long/65536.0 - 0.5)*60
        self.Ygauss = (self.Ybyte2long/65536.0 - 0.5)*60
        self.Zgauss = (self.Zbyte2long/65536.0 - 0.5)*60
        return [self.Xgauss,self.Ygauss,self.Zgauss]
