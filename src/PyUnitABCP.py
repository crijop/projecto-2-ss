'''
Created on 2013/01/14

@author: admin1
'''





def assertEqualsPy(expected, actual):
    if not type(expected) == type(actual):
        print "false"
        return False
    else:
        print "vrdd"
        return True

assertEqualsPy(1, "oala") 
    