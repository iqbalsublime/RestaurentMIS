# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:16:24 2019

@author: iqbalsublime
"""

class Reserve:


    # Initializer / Instance Attributes
    def __init__(self, reserveid, date, customer,restaurent):
        self.reserveid = reserveid
        self.date = date
        self.customer = customer
        self.restaurent = restaurent


    def getReserve(self):
        return self.name
    
    # instance method
    def description(self):
        return "Reserve ID:{}, Date: {} Customer: {} Branch: {}".format(self.reserveid, self.date, self.customer, self.restaurent)

