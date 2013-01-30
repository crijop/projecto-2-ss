#-*- coding:utf-8 -*-
'''
Created on 2013/01/14

@author: admin1
'''
from inspect import getframeinfo, currentframe, ismethod
from interface import *
import inspect
import parser
import wx



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
    methodsList = []
    #beginTest(classObject)
    
    class Test(object):
    
        def __init__(self, function):
            self.function = function
            #print "fazer Teste"
            PyUniti.methodsList.append(self.function)
            #self.__call__()
            pass
        
        '''def __call__(self):
            
            print "fazer Teste CALL"
            
            global isTest
            isTest = True
            PyUniti.failsList.append(PyUniti.TestStatus(self.function.__name__))
            #self.function(self)
            isTest = False
            PyUniti.failsListPosition += 1
            pass'''
        
    
    def __init__(self):
        #print "possst"
        #self.failsList = []
        #self.failsListPossition = 0
        #self.beginTest(classObject)
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        self.frame_1 = PyUnitiABCP(None, -1, "")
        app.SetTopWindow(self.frame_1)
     
        self.frame_1.Show()
        
        self.frame_1.setMethodsList(PyUniti.methodsList, self.check_Method, self.start_Test, self.selChanged, self.exitProgram)
        
        self.frame_1.Show()
        app.MainLoop()
        
        
        
        '''for me in PyUniti.methodsList:
            global isTest
            isTest = True
            print me.__name__
            PyUniti.failsList.append(PyUniti.TestStatus(me.__name__))
            me(self)
            isTest = False
            PyUniti.failsListPosition += 1'''
        
        #print "Teste linha", PyUniti.failsList[1].getTestList()[0].getLineNumber()
        
        pass
    def check_Method(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        
        
        if(self.frame_1.getAllMethodsCheckBox().IsChecked() == True):
            self.frame_1.getAllMethodsCheckBox().SetValue(False)
            
        event.Skip()
        
    def start_Test(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
    
        PyUniti.failsList = []
        PyUniti.failsListPosition = 0
        self.frame_1.removeTreeElements()
        self.frame_1.Show()
        for chekBoxMethods in self.frame_1.getAllCheckBox():
            if(chekBoxMethods.IsChecked() == True):
                pos = self.frame_1.getAllCheckBox().index(chekBoxMethods)
                PyUniti.failsList.append(PyUniti.TestStatus(PyUniti.methodsList[pos].__name__))
                PyUniti.methodsList[pos](self)
                
                PyUniti.failsListPosition += 1
                #print "olaa"
        
        self.frame_1.makeTree(PyUniti.failsList)
        self.frame_1.Show()
                
        
        event.Skip()
        
    def exitProgram(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        if wx.MessageBox("Deseja sair do programa?", "Confirmar", wx.YES_NO) == wx.YES :
            #print "sair"
            exit(0)
            pass
        #event.Skip()
            
    def selChanged(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        item =  event.GetItem()
        parent = self.frame_1.getTree().GetItemParent(item)
        
        teste = self.frame_1.getTree().GetPyData(item)
        classe = self.frame_1.getTree().GetPyData(parent)
        
        if classe == None:
            isFail = 0
            for testes in teste.getTestList():
                if testes.getStatus() == False:
                    isFail += 1
                    
            
            self.frame_1.makeMethodStatistics(teste.getFunctionName(), isFail)
            
            
        elif teste.getType() == 2:
            self.frame_1.makeEqualsStatistics(classe.getFunctionName(), teste.getExpected(), teste.getExpectedType(), teste.getActual(), teste.getActualType(), teste.getLineNumber(), teste.getName(), teste.getStatus(), teste.getFailMensage())
        elif teste.getType() == 3:
            self.frame_1.makeTrueFalseStatistics(classe.getFunctionName(), teste.getCondition(), teste.getLineNumber(), teste.getName(), teste.getStatus(), teste.getFailMensage())    
        
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
                PyUniti.methodsList.append(attribute)
                attribute()
                #print "nada"
                
                
    class TestStatus():
        def __init__(self, functionName):
            self.testList = []
            self.functionName = functionName
        
        def getType(self):
                return 1
                pass
                
        def addTest(self, test):
            self.testList.append(test)
            
        def addFunctionName(self, functionName):
            self.functionName = functionName
            pass
        def getFunctionName(self):
            return self.functionName
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
            #if isTest == True:
            if type(condition) == bool:
                if condition == False:
                    mensage += "A variavél é Falsa"
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = True
                   
                else:
                    mensage += "A variavél é Verdadeira"
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = False
                    
                pass
            else:
                mensage += "A variavél não é do tipo Booleana"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = False
                
                pass
            pass
            #else:
                #mensage += "Não se verifica um teste (@Test)"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                #pass
            
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertFalsePy(condition, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            pass
            
        '''
        AssertTruePy
        '''
        @staticmethod    
        def assertTruePy(condition):
            mensage = ""
            status = False
            lineNumber = None
            #if isTest == True:
            if type(condition) == bool:
                if condition == True:
                    mensage += "A variavél é verdadeira"
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = True
                    
                else:
                    mensage += "A variavél é falsa"
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    status = False
                    
                pass
            else:
                mensage += "A variavél não é do tipo Booleana"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = False
                    
                pass
                
           
                
            #else:
                #mensage += "Não se verifica um teste (@Test)"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                #pass
            
            
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertTruePy(condition, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            pass
           
        '''
        AssertEqualsPy
        '''
        @staticmethod
        def assertEqualsPy(expected, actual):
            mensage = ""
            expectedType = str(type(expected))
            actualType = str(type(actual))
            status = False
            lineNumber = None
            #if isTest == True:
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
            #else:
        
                #print "não é teeste"
             
                #mensage += "Não se verifica um teste (@Test)"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                #pass
            
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertEqualsPy(expected, actual, expectedType, actualType, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            
            pass
            
        class AssertEqualsPy(object):
    
            def __init__(self, expected, actual, expectedType, actualType, lineNumber, status, failMensage):
                self.expected = expected
                self.actual = actual
                self.expectedType = expectedType
                self.actualType = actualType
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertEquals"
                self.failMensage = failMensage
                
            
            def getFailMensage(self):
                #print self.failMensage
                return self.failMensage
                pass
            
            def getExpectedType(self):
                return self.expectedType
                pass
            
            def getActualType(self):
                return self.actualType
                pass
            
            def getType(self):
                return 2
                pass
            def getName(self):
                return self.name
                pass
                
            def getActual(self):
                
                return self.actual
            
            def getExpected(self):
                
                return self.expected
            
            def getLineNumber(self):
                
                return self.lineNumber
                pass
            
            def getStatus(self):
                
                return self.status
                pass
            
            pass
        
        class AssertTruePy(object):
    
            def __init__(self, condition, lineNumber, status, failMensage):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertTrue"
                self.failMensage = failMensage
            
            def getFailMensage(self):
                
                return self.failMensage
                pass
            
            def getType(self):
                return 3
                pass
            
            def getName(self):
                return self.name
                pass
                
            def getCondition(self):
                
                return self.condition
            
            def getLineNumber(self):
                
                return self.lineNumber
            
            def getStatus(self):
                
                return self.status
            
            
            pass
        
        class AssertFalsePy(object):
    
            def __init__(self, condition, lineNumber, status, failMensage):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertFalse"
                self.failMensage = failMensage
            
            def getFailMensage(self):
                
                return self.failMensage
                pass
            def getType(self):
                return 3
                pass
            
            def getName(self):
                return self.name
                pass
                
                
            def getCondition(self):
                
                return self.condition
            
            def getLineNumber(self):
                
                return self.lineNumber
            
            def getStatus(self):
                
                return self.status
            
            
            pass
                       
                           
                                    
                                
                            