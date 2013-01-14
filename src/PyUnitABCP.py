#-*- coding:utf-8 -*-
'''
Created on 2013/01/14

@author: admin1
'''



isTest = False
        
    


class Test(object):
    
    def __init__(self, function):
        self.function = function
        pass
    
    def __call__(self):
        global isTest
        isTest = True
        print isTest
        self.function()
        isTest = False
        pass
    



def assertEqualsPy(expected, actual):
    if isTest == True:
        if not type(expected) == type(actual):
            print "false"
            return False
        else:
            if expected == actual:
                print "true"
                return True
            else:
                print "false 2"
                return False
    else:
        
        print "não é teeste"
                
            

