#-*- coding:utf-8 -*-
'''
Created on 2013/01/14

@author: admin1
'''
from inspect import getframeinfo, currentframe
import inspect
from inspect import ismethod
import parser



isTest = False
#failsListPossition = 0
'''
def addFile(file):
    
    for name in dir(file):
        attribute = getattr(file, name)
        if ismethod(attribute):
            print "ola"
            attribute()
           
    pass
'''
 
    
    
'''           
def getFails():
    
    for test in failsList:
        print test.getFunctionName
        test.getTestList()
        
    return failsList'''


    




 
class PyUniti(object):
    
    #global ola
    #ola = "SOU SELF OLAAAAAAAAAAAAA"
    failsList = []
    failsListPosition = 0
    #beginTest(classObject)
    
    class Test(object):
    
        def __init__(self, function):
            self.function = function
            #print "fazer Teste"
            self.__call__()
            pass
        
        def __call__(self):
            
            #print "fazer Teste CALL"
            
            global isTest
            isTest = True
            PyUniti.failsList.append(PyUniti.TestStatus(self.function.__name__))
            self.function(self)
            isTest = False
            PyUniti.failsListPosition += 1
            pass
        
    
    def __init__(self, classObject):
        #self.failsList = []
        #self.failsListPossition = 0
        self.beginTest(classObject)
        
        print "Teste linha", PyUniti.failsList[1].getTestList()[0].getLineNumber()
        
        pass
    
    
    def get_failList(self):
        return self.failsList
        pass
    
    @staticmethod
    def set_failList():
        #global ola
        #print "OLa sou set", PyUniti.ola
        pass
    
    def beginTest(self, classObject ):
        for name in dir(classObject):
            attribute = getattr(classObject, name)
            if ismethod(attribute):
                attribute()
                
                
    class TestStatus():
        def __init__(self, functionName):
            self.testList = []
            self.functionName = functionName
            
        def addTest(self, test):
            self.testList.append(test)
            
        def addFunctionName(self, functionName):
            self.functionName = functionName
            pass
        def getTestList(self):
            
            return self.testList
    
    class UnitiTests(object):
        
        '''
        AssertFalsePy
        '''
        @staticmethod
        def assertFalsePy(condition):
            mensage = ""
            status = False
            lineNumber = None
            if isTest == True:
                if type(condition) == bool:
                    if condition == False:
                        mensage += "A variavél é Falsa"
                        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        status = True
                       
                    else:
                        mensage += "A variavél é Verdadeira"
                        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        status = False
                        
                    pass
                else:
                    mensage += "A variavél não é do tipo Booleana"
                    print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = False
                    
                    pass
                pass
            else:
                mensage += "Não se verifica um teste (@Test)"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                pass
            
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertTruePy(condition, lineNumber, status))
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            pass
            
        '''
        AssertTruePy
        '''
        @staticmethod    
        def assertTruePy(condition):
            mensage = ""
            status = False
            lineNumber = None
            if isTest == True:
                if type(condition) == bool:
                    if condition == True:
                        mensage += "A variavél é verdadeira"
                        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        status = True
                        
                    else:
                        mensage += "A variavél é falsa"
                        print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        status = False
                        
                    pass
                else:
                    mensage += "A variavél não é do tipo Booleana"
                    print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = False
                    
                    pass
                
           
                
            else:
                mensage += "Não se verifica um teste (@Test)"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                pass
            
            
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertTruePy(condition, lineNumber, status))
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            pass
           
        '''
        AssertEqualsPy
        '''
        @staticmethod
        def assertEqualsPy(expected, actual):
            mensage = ""
            status = False
            lineNumber = None
            if isTest == True:
                if not type(expected) == type(actual):
                    mensage += "O tipo das variáveis inseridas não é igual"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    #status = False
                else:
                    if expected == actual:
                        mensage += "O Valor do AssertEqualsPY está correcto"
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        status = True
                    else:
                        mensage += "O Valor do AssertEqualsPY está errado"
                        lineNumber = inspect.currentframe().f_back.f_lineno
                        #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                        status = False
                        
            
                
                #global failsList
                #PyUniti.set_failList()
                #PyUniti.failsList[PyUniti.failsListPossition].addTest(PyUniti.AssertEqualsPy(expected, actual, lineNumber, status))
            else:
        
                print "não é teeste"
             
                mensage += "Não se verifica um teste (@Test)"
                print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                pass
            
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertEqualsPy(expected, actual, lineNumber, status))
            print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            
            pass
            
        class AssertEqualsPy(object):
    
            def __init__(self, expected, actual, lineNumber, status):
                self.expected = expected
                self.actual = actual
                self.lineNumber = lineNumber
                self.status = status
                
            def getActual(self):
                
                return self.actual
            
            def getExpected(self):
                
                return self.expected
            
            def getLineNumber(self):
                
                return self.lineNumber
            
            def getStatus(self):
                
                return self.status
            
            
            pass
        
        class AssertTruePy(object):
    
            def __init__(self, condition, lineNumber, status):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                
            def getCondition(self):
                
                return self.condition
            
            def getLineNumber(self):
                
                return self.lineNumber
            
            def getStatus(self):
                
                return self.status
            
            
            pass
        
        class AssertFalsePy(object):
    
            def __init__(self, condition, lineNumber, status):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                
            def getCondition(self):
                
                return self.condition
            
            def getLineNumber(self):
                
                return self.lineNumber
            
            def getStatus(self):
                
                return self.status
            
            
            pass
                       
                           
                                    
                                
                            