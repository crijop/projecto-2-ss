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


'''
Classe responsavel por tratar todos os testes
e intrepertar a informação passada pelo utilizador
bem como enviar informação para a interface gráfica
''' 
class PyUniti(object):
    
    #global ola
    #ola = "SOU SELF OLAAAAAAAAAAAAA"
    failsList = []
    failsListPosition = 0
    methodsList = []
    #beginTest(classObject)
    '''
    Classe responsavel pelo decorator que se introduz 
    no inicio de cada método
    para indicar que o mesmo é de teste
    '''
    class Test(object):
    
        '''
        Adiciona os métodos a uma lista
        '''
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
        
    ''' Construtir da classe principal onde é inicizalida 
    uma instancia da interface gráfica
    '''
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
    '''
    Verfica se a checboz está selecionada ou não quando
    clicada
    '''
    def check_Method(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        
        
        if(self.frame_1.getAllMethodsCheckBox().IsChecked() == True):
            self.frame_1.getAllMethodsCheckBox().SetValue(False)
            
        event.Skip()
    
    '''
    Função responsavel pelo inicio do
    teste as funções seleciondas na interface gráfica
    '''    
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
    '''
    Trata do envento de saida do programa
    '''    
    def exitProgram(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        if wx.MessageBox("Deseja sair do programa?", "Confirmar", wx.YES_NO) == wx.YES :
            #print "sair"
            exit(0)
            pass
        #event.Skip()
    '''
    Tarata dos eventos dos nós da árvore
    '''        
    def selChanged(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        item =  event.GetItem()
        parent = self.frame_1.getTree().GetItemParent(item)
        
        teste = self.frame_1.getTree().GetPyData(item)
        classe = self.frame_1.getTree().GetPyData(parent)
        print self.frame_1.getTree().ItemHasChildren(item)
        if parent != None:
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
    '''
    Devolve a lista de testes
    '''    
    def get_failList(self):
        return self.failsList
        pass
    
    
    '''def beginTest(self, classObject ):
        for name in dir(classObject):
            attribute = getattr(classObject, name)
            if ismethod(attribute):
                PyUniti.methodsList.append(attribute)
                attribute()
                print "nada"'''
                
    '''
    Sub classe responsavel por guardar informação de cada  método
    '''            
    class TestStatus():
        '''
        define a lista de testes e guarda o nome da função
        '''
        def __init__(self, functionName):
            self.testList = []
            self.functionName = functionName
        
        '''classifica a classe com um tipo
        '''
        def getType(self):
                return 1
                pass
        '''
        adiciona os testes
        presentes na funmção a lista de testes
        '''
        def addTest(self, test):
            self.testList.append(test)
        '''
        Adiciona o nome da função
        '''    
        def addFunctionName(self, functionName):
            self.functionName = functionName
            pass
        '''
        Retorna o nome da função
        '''
        def getFunctionName(self):
            return self.functionName
            pass
        '''
        Retorna a lista de testes
        '''
        def getTestList(self):
            
            return self.testList
    
    '''
    Subclasse onde tem os métodos estáticos de teste
    que serão chamados pelo utilzador
    '''
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
        AssertNotNullPy
        '''
        @staticmethod    
        def assertNotNullPy(condition):
            mensage = ""
            status = False
            lineNumber = None
            #if isTest == True:
            if condition == None:
                mensage += "A variavel é Nula"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = False
                
            else:
                mensage += "A variavél não é Nula"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = True
                
            pass
       
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertNotNullPy(condition, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            pass
        
        '''
        AssertNullPy
        '''
        @staticmethod    
        def assertNullPy(condition):
            mensage = ""
            status = False
            lineNumber = None
            #if isTest == True:
            if condition == None:
                mensage += "A variavel é Nula"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = True
                
            else:
                mensage += "A variavél não é Nula"
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                lineNumber = inspect.currentframe().f_back.f_lineno
                status = False
                
            pass
       
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertNullPy(condition, lineNumber, status, mensage))
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
                status = False
            else:
                if expected == actual:
                    mensage += "O Valor esperado «" + str(expected) +"» é igual ao valor atual «" + str(actual) + "»"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = True
                else:
                    mensage += "O Valor esperado «" + str(expected) +"» não é igual ao valor atual «" + str(actual) + "»"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = False
    
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertEqualsPy(expected, actual, expectedType, actualType, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            
            pass
        '''
        AssertNotSamePy
        '''
        @staticmethod
        def assertNotSamePy(unexpected, actual):
            mensage = ""
            expectedType = str(type(unexpected))
            actualType = str(type(actual))
            status = False
            lineNumber = None
            #if isTest == True:
            if not type(unexpected) == type(actual):
                mensage += "O tipo das variáveis inseridas não é igual"
                lineNumber = inspect.currentframe().f_back.f_lineno
                #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                status = True
            else:
                if unexpected is actual:
                    mensage += "O Valor não esperado «" + str(unexpected) +"» não se refere ao mesmo objecto que o valor atual «" + str(actual) + "»"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = False
                else:
                    mensage += "O Valor não esperado «" + str(unexpected) +"» refere-se ao mesmo objecto que o valor atual «" + str(actual) + "»"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = True
    
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertNotSamePy(unexpected, actual, expectedType, actualType, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            
            pass
        
        '''
        AssertSamePy
        '''
        @staticmethod
        def assertSamePy(expected, actual):
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
                status = False
            else:
                if expected is actual:
                    mensage += "O valor esperado <" + str(expected) + "> e o valor actual <" + str(actual) + "> referem-se ao mesmo objecto"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = True
                else:
                    mensage += "O Valor esperado «" + str(expected) +"» não se refere ao mesmo objecto que o valor atual «" + str(actual) + "»"
                    lineNumber = inspect.currentframe().f_back.f_lineno
                    #print mensage, " na linha: ", inspect.currentframe().f_back.f_lineno
                    status = False
    
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            PyUniti.failsList[PyUniti.failsListPosition].addTest(PyUniti.UnitiTests.AssertSamePy(expected, actual, expectedType, actualType, lineNumber, status, mensage))
            #print "oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", PyUniti.failsListPosition
            
            pass
        ############################################################################
        ############################################################################
        '''
        Classe que guarda informação 
        sobre o assertEquals
        '''        
        class AssertEqualsPy(object):
    
            '''
            Construtor onde são adiconados todos os elementes que constituem este eteste
            '''
            def __init__(self, expected, actual, expectedType, actualType, lineNumber, status, failMensage):
                self.expected = expected
                self.actual = actual
                self.expectedType = expectedType
                self.actualType = actualType
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertEquals"
                self.failMensage = failMensage
                
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                #print self.failMensage
                return self.failMensage
                pass
           
            '''
            retorna o tipo valor esperado
            '''
            def getExpectedType(self):
                return self.expectedType
                pass
            '''
            retorna o tipo valor actual
            '''
            def getActualType(self):
                return self.actualType
                pass
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 2
                pass
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
            '''
            retorna no valor
            actual
            '''
            def getActual(self):
                
                return self.actual
            '''
            retorna o valor esperado
            '''
            def getExpected(self):
                
                return self.expected
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
                pass
            '''
            devolve o estado
            se passou ou não o teste
            '''
            def getStatus(self):
                
                return self.status
                pass
            
            pass
        '''
        Classe que guarda informação 
        sobre o AssertNotSamePy
        '''      
        class AssertNotSamePy(object):
            '''
            Construtor onde são adiconados todos os elementes que constituem este eteste
            '''
            def __init__(self, expected, actual, expectedType, actualType, lineNumber, status, failMensage):
                self.expected = expected
                self.actual = actual
                self.expectedType = expectedType
                self.actualType = actualType
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertNotSame"
                self.failMensage = failMensage
                
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                #print self.failMensage
                return self.failMensage
                pass
           
            '''
            retorna o tipo valor esperado
            '''
            def getExpectedType(self):
                return self.expectedType
                pass
            '''
            retorna o tipo valor actual
            '''
            def getActualType(self):
                return self.actualType
                pass
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 2
                pass
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
                
            '''
            retorna no valor
            actual
            '''
            def getActual(self):
                
                return self.actual
            
            '''
            retorna o valor esperado
            '''
            def getExpected(self):
                
                return self.expected
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
                pass
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
            def getStatus(self):
                
                return self.status
                pass
            
            pass
        
        class AssertSamePy(object):
    
            def __init__(self, expected, actual, expectedType, actualType, lineNumber, status, failMensage):
                self.expected = expected
                self.actual = actual
                self.expectedType = expectedType
                self.actualType = actualType
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertSame"
                self.failMensage = failMensage
                
            
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                #print self.failMensage
                return self.failMensage
                pass
            
            
            '''
            retorna o tipo valor esperado
            '''
            def getExpectedType(self):
                return self.expectedType
                pass
            
            '''
            retorna o tipo valor actual
            '''
            def getActualType(self):
                return self.actualType
                pass
            
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 2
                pass
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
                
            '''
            retorna no valor
            actual
            '''
            def getActual(self):
                
                return self.actual
            
            '''
            retorna o valor esperado
            '''
            def getExpected(self):
                
                return self.expected
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
                pass
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
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
            
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                
                return self.failMensage
                pass
            
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 3
                pass
            
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
            '''
            retorna a condição
            '''    
            def getCondition(self):
                
                return self.condition
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
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
            
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                
                return self.failMensage
                pass
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 3
                pass
            
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
                
            '''
            retorna a condição
            '''      
            def getCondition(self):
                
                return self.condition
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
            def getStatus(self):
                
                return self.status
            
            
            pass
        
        class AssertNotNullPy(object):
    
            def __init__(self, condition, lineNumber, status, failMensage):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertNotNull"
                self.failMensage = failMensage
            
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                
                return self.failMensage
                pass
            
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 3
                pass
            
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
            '''
            retorna a condição
            '''      
            def getCondition(self):
                
                return self.condition
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
            def getStatus(self):
                
                return self.status
            
            
            pass
        
        class AssertNullPy(object):
    
            def __init__(self, condition, lineNumber, status, failMensage):
                self.condition = condition
                self.lineNumber = lineNumber
                self.status = status
                self.name = "AssertNull"
                self.failMensage = failMensage
            
            '''
            Retorna a mensagem
            de errro
            '''
            def getFailMensage(self):
                
                return self.failMensage
                pass
            
            '''
            retorna o tipo da classe para efeitos de controlo
            '''
            def getType(self):
                return 3
                pass
            
            '''
            retorna o nome da classe de teste
            '''
            def getName(self):
                return self.name
                pass
            '''
            retorna a condição
            '''      
            def getCondition(self):
                
                return self.condition
            
            '''
            retorna o numero da linha do teste
            '''
            def getLineNumber(self):
                
                return self.lineNumber
            
            '''
            devolve o estado
            se passou ou não o teste
            '''
            def getStatus(self):
                
                return self.status
            
            
            pass
                       
                           
                                    
                                
                            