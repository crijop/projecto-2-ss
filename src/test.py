#-*- coding:utf-8 -*-
'''
Created on 14 de Jan de 2013

@author: xama
'''

from PyUnitABCP import *


class PTestes():
    
    @PyUniti.Test
    def primeiroTeste(self):    
        i = 5
        #print "Primeiro Teste"
        PyUniti.UnitiTests.assertEqualsPy("vgh", i)
    
        array = [1, 2, 4]
        i = "carlos"
        a = 1
       
        PyUniti.UnitiTests.assertEqualsPy("carlos", i)
        PyUniti.UnitiTests.assertEqualsPy(1, a)
        PyUniti.UnitiTests.assertEqualsPy(array, [1, 2, 4, 4])
        
        pass
    
    @PyUniti.Test
    def segundoTeste(self):
        #print "\nSegundo Teste, faz o assertTruePy"
        a = 9
        PyUniti.UnitiTests.assertTruePy(10<a)
        pass
    
    @PyUniti.Test
    def terceiroTeste(self):
        #print "\nTerceiro Teste, faz o assertFalsePy"
        a = 8
        PyUniti.UnitiTests.assertFalsePy(3 < a)
        pass
    

    @PyUniti.Test
    def quartoTeste(self):
        #print "\nTerceiro Teste, faz o assertFalsePy"
        var = True
        PyUniti.UnitiTests.assertFalsePy(var)
        pass
    pass
pass

if __name__ == "__main__":
    PyUniti()
    pass



