# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:16:24 2019

@author: iqbalsublime
"""

class Customer:


    # Initializer / Instance Attributes
    def __init__(self, cid, name, mobile,waiter):
        self.cid = cid
        self.name = name
        self.mobile = mobile
        self.waiter = waiter


    def getCustomerName(self):
        return self.name
    
    # instance method
    def description(self):
        return "{}'s Mobile: {}".format(self.name, self.mobile)

#cust1= Customer(1,"Iqbal", "0167****671")
#print(cust1.description())