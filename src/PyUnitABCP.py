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
        self.function()
        isTest = False
        pass
    

def assertEqualsPy(expected, actual):
    mensage = ""
    if isTest == True:
        if not type(expected) == type(actual):
            mensage += "O tipo das variáveis inseridas não é igual"
            print mensage
            return False
        else:
            if expected == actual:
                mensage += "O Valor do AssertEqualsPY está correcto"
                print mensage
                return True
            else:
                mensage += "O Valor do AssertEqualsPY está errado"
                print mensage
                return False
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage
        pass
    pass
                
def assertTruePy(condition):
    mensage = ""
    if isTest == True:
        if type(condition) == bool:
            if condition == True:
                mensage += "A variavél é verdadeira"
                print mensage
                return True
            else:
                mensage += "A variavél é falsa"
                print mensage
                return False
            pass
        else:
            mensage += "A variavél não é do tipo Booleana"
            print mensage
            return False
            pass
        pass
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage
        pass
    pass

def assertFalsePy(condition):
    mensage = ""
    if isTest == True:
        if type(condition) == bool:
            if condition == False:
                mensage += "A variavél é Falsa"
                print mensage
                return True
            else:
                mensage += "A variavél é Verdadeira"
                print mensage
                return False
            pass
        else:
            mensage += "A variavél não é do tipo Booleana"
            print mensage
            return False
            pass
        pass
    else:
        mensage += "Não se verifica um teste (@Test)"
        print mensage
        pass
            
    