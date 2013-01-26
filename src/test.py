#-*- coding:utf-8 -*-
'''
Created on 14 de Jan de 2013

@author: xama
'''

from PyUnitABCP import *


class testar():
    
    @PyUniti.Test
    def primeiroTeste(self):    
        i = 5
        print "Primeiro Teste"
        PyUniti.UnitiTests.assertEqualsPy("vgh", i)
    
        array = [1, 2, 4]
        i = "carlos"
        a = 1
        '''
        PyUniti.UnitiTests.assertEqualsPy("carlos", i)
        PyUniti.UnitiTests.assertEqualsPy(1, a)
        PyUniti.UnitiTests.assertEqualsPy(array, [1, 2, 4, 4])
        '''
        pass
    
        
    
    
    @PyUniti.Test
    def segundoTeste(self):
        print "\nSegundo Teste, faz o assertTruePy"
        var = True
        PyUniti.UnitiTests.assertTruePy(var)
        pass
    
    @PyUniti.Test
    def terceiroTeste(self):
        print "\nTerceiro Teste, faz o assertFalsePy"
        var = False
        PyUniti.UnitiTests.assertFalsePy(var)
        pass

if __name__ == "__main__":
    PyUniti(testar())
    pass



