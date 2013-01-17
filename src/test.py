#-*- coding:utf-8 -*-
'''
Created on 14 de Jan de 2013

@author: xama
'''

from PyUnitABCP import *


class testar(PyUniti.UnitiTests):
    
    @PyUniti.Test
    def primeiroTeste(self):    
        i = 5
    
        print "teste", self.assertEqualsPy("vgh", i)
    
        array = [1, 2, 4]
        i = "carlos"
        a = 1
        self.assertEqualsPy("carlos", i)
        self.assertEqualsPy(1, a)
        self.assertEqualsPy(array, [1, 2, 4, 4])
    
        pass
    
        
    
    
    @PyUniti.Test
    def segundoTeste(self):
        print "KO"
        var = True
        self.assertTruePy(var)
        pass
    
    @PyUniti.Test
    def terceiroTeste(self):
        var = False
        self.assertFalsePy(var)
        pass

if __name__ == "__main__":
    PyUniti(testar())
    pass



