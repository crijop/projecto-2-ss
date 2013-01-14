#-*- coding:utf-8 -*-
'''
Created on 14 de Jan de 2013

@author: xama
'''

from PyUnitABCP import *

dir()

@Test
def primeiroTeste():
    
    array = [1, 2, 4]
    i = "carlos"
    a = 1
    assertEqualsPy("carlos", i)
    assertEqualsPy(1, a)
    assertEqualsPy(array, [1, 2, 4, 4])
    pass

@Test
def segundoTeste():
    var = True
    assertTruePy(var)
    pass

@Test
def terceiroTeste():
    var = False
    assertFalsePy(var)
    pass

if __name__ == "__main__":
    primeiroTeste()
    segundoTeste()
    terceiroTeste()
    pass


    