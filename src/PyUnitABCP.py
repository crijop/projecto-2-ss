#-*- coding:utf-8 -*-
'''
Created on 2013/01/14

@author: admin1
'''
from inspect import getframeinfo, currentframe
import inspect



isTest = False
        
    


class Test(object):
    
    def __init__(self, function):
        self.function = function
        pass
    
    def __call__(self):
        global isTest
        isTest = True
        self.function()
        isTest = False
        pass
    

def assertEqualsPy(expected, actual):
    mensage = ""
    if isTest == True:
        if not type(expected) == type(actual):
            mensage += "O tipo das variáveis inseridas não é igual"
            print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
            return False
        else:
            if expected == actual:
                mensage += "O Valor do AssertEqualsPY está correcto"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return True
            else:
                mensage += "O Valor do AssertEqualsPY está errado"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return False
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
        pass
    pass
                
def assertTruePy(condition):
    mensage = ""
    if isTest == True:
        if type(condition) == bool:
            if condition == True:
                mensage += "A variavél é verdadeira"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return True
            else:
                mensage += "A variavél é falsa"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return False
            pass
        else:
            mensage += "A variavél não é do tipo Booleana"
            print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
            return False
            pass
        pass
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
        pass
    pass

def assertFalsePy(condition):
    mensage = ""
    if isTest == True:
        if type(condition) == bool:
            if condition == False:
                mensage += "A variavél é Falsa"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return True
            else:
                mensage += "A variavél é Verdadeira"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                return False
            pass
        else:
            mensage += "A variavél não é do tipo Booleana"
            print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
            return False
            pass
        pass
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
        pass
            
    