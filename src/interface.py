#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Mon Jan 28 17:52:01 2013

import wx

# begin wxGlade: extracode
# end wxGlade


class PyUnitiABCP(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PyUnitiABCP.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.panel_6 = wx.ScrolledWindow(self.notebook_1_pane_1, -1, style=wx.TAB_TRAVERSAL)
        self.panel_7 = wx.Panel(self.panel_6, -1)
        self.all_metodos_box = wx.CheckBox(self.panel_7, -1, "")
        self.label_4 = wx.StaticText(self.panel_7, -1, "Metodos a executar")
        self.label_4.SetForegroundColour('White')
        #self.checkbox_13 = wx.CheckBox(self.panel_6, -1, "checkbox_13")
        #self.checkbox_14 = wx.CheckBox(self.panel_6, -1, "checkbox_14")
        self.button_5 = wx.Button(self.notebook_1_pane_1, -1, "Iniciar Teste")
        self.panel_9 = wx.Panel(self.notebook_1_pane_1, -1)
        self.button_6 = wx.Button(self.notebook_1_pane_1, -1, "Sair")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.tree = wx.TreeCtrl(self.notebook_1_pane_2, -1, style=wx.TR_HAS_BUTTONS | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)
        self.panel_1 = wx.Panel(self.notebook_1_pane_2, -1)
        self.label_1 = wx.StaticText(self.panel_1, -1, "Resultados", style=wx.ALIGN_CENTRE)
        self.label_1.SetForegroundColour('White')
        self.panel_2 = wx.ScrolledWindow(self.notebook_1_pane_2, -1, style=wx.TAB_TRAVERSAL)
        
        #self.panel_3 = wx.Panel(self.notebook_1_pane_2, -1)
        self.label_7 = wx.StaticText(self.panel_2, -1, "Sem Resultados")
        
        
        self.panel_3 = wx.Panel(self.panel_2, -1)
        #self.button_1 = wx.Button(self.panel_2, -1, "Sair")

        self.__set_properties()
        
        self.listMethods_checkBoxs = []

        self.Bind(wx.EVT_CHECKBOX, self.checkAll_Methods, self.all_metodos_box)
        
        
        #self.Bind(wx.EVT_BUTTON, self.exitProgram, self.button_6)
        
        
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PyUnitiABCP.__set_properties
        self.SetTitle("PyUnitiABCP")
        self.SetSize((550, 400))
        self.label_4.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.panel_7.SetBackgroundColour(wx.Colour(50, 153, 204))
        self.panel_6.SetScrollRate(10, 10)
        self.panel_2.SetScrollRate(10, 10)
        self.tree.SetMinSize((225, 276))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panel_1.SetBackgroundColour(wx.Colour(50, 153, 204))
        # end wxGlade

    def __do_layout(self, methodEventCheckBox):
        # begin wxGlade: PyUnitiABCP.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.VERTICAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21.Add(self.all_metodos_box, 0, 0, 0)
        sizer_21.Add(self.label_4, 0, 0, 0)
        self.panel_7.SetSizer(sizer_21)
        sizer_20.Add(self.panel_7, 0, wx.EXPAND, 0)
        #sizer_20.Add(self.checkbox_13, 0, 0, 0)
        #sizer_20.Add(self.checkbox_14, 0, 0, 0)
        
        for methods in self.listMethods:
            self.checkbox_13 = wx.CheckBox(self.panel_6, -1, "" + str(methods.__name__))
            sizer_20.Add(self.checkbox_13, 0, 0, 0)
            self.listMethods_checkBoxs.append(self.checkbox_13)
            self.Bind(wx.EVT_CHECKBOX, methodEventCheckBox, self.checkbox_13)
            
        
        self.panel_6.SetSizer(sizer_20)
        sizer_17.Add(self.panel_6, 1, wx.EXPAND, 0)
        sizer_23.Add(self.button_5, 0, wx.EXPAND, 0)
        sizer_23.Add(self.panel_9, 1, wx.EXPAND, 0)
        sizer_23.Add(self.button_6, 0, wx.EXPAND, 0)
        sizer_17.Add(sizer_23, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_17)
        sizer_2.Add(self.tree, 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 11)
        self.panel_1.SetSizer(sizer_4)
        sizer_3.Add(self.panel_1, 0, wx.EXPAND, 0)
        self.sizer_8.Add(self.label_7, 0, 0, 0)
        #self.sizer_8.Add(self.label_8, 0, 0, 0)
        #self.sizer_8.Add(self.label_9, 0, 0, 0)
        #self.sizer_8.Add(self.label_10, 0, 0, 0)
        
        
        
        self.sizer_8.Add(self.panel_3, 1, wx.EXPAND, 0)
        #self.sizer_8.Add(self.button_1, 0, wx.EXPAND, 0)
        self.panel_2.SetSizer(self.sizer_8)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)
        #sizer_3.Add(self.panel_3, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Metodos Teste")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Resultado Teste")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
        
    def makeTree(self, failsList):
        
        root = self.tree.AddRoot('Teste')
        for method in failsList:
            
            classe = wx.TreeItemData()
            classe.SetData(method)
            metodo = self.tree.AppendItem(root, '' + str(method.getFunctionName()), -1,-1, classe)
            #metodo.
            for test in method.getTestList():
                data = wx.TreeItemData()
                data.SetData(test)
                no = self.tree.AppendItem(metodo, '' + "<"+str(test.getLineNumber())+"> " + str(test.getName()), -1, -1, data)
                
            '''
            self.tree.AppendItem(os, 'FreeBSD')
            self.tree.AppendItem(os, 'OpenBSD')
            self.tree.AppendItem(os, 'NetBSD')
            self.tree.AppendItem(os, 'Solaris')
            cl = self.tree.AppendItem(pl, 'Compiled languages')
            sl = self.tree.AppendItem(pl, 'Scripting languages')
            self.tree.AppendItem(cl, 'Java')
            self.tree.AppendItem(cl, 'C++')'''

    def makeEqualsStatistics(self, funcName, expected, expectedType, actual, actualType, lineNumber, name, status, failMensage):
        self.sizer_8.Clear(True)
        
        self.func = wx.StaticText(self.panel_2, -1, "Método: " + str(funcName))
        self.func.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.type = wx.StaticText(self.panel_2, -1, "\nTipo: " + str(name))
        self.type.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        if(status == True):
            self.status = wx.StaticText(self.panel_2, -1, "\n\nEstado: Passou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
            self.status.SetForegroundColour((0,128,0))
        else:
            self.status = wx.StaticText(self.panel_2, -1, "\n\nEstado: Falhou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans")) 
            self.status.SetForegroundColour((255,0,0))
        
        self.expected = wx.StaticText(self.panel_2, -1, "\n\n\nValor Esperado: " + str(expected))
        self.expected.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.expectedType = wx.StaticText(self.panel_2, -1, "\n\n\n\nValor Esperado Tipo:\n" + str(expectedType))
        self.expectedType.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        self.actual = wx.StaticText(self.panel_2, -1, "\n\n\n\n\n\n\nValor Actual: " + str(actual))
        self.actual.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.actualType = wx.StaticText(self.panel_2, -1, "\n\n\n\n\n\n\n\nValor Actual Tipo:\n" + str(actualType))
        self.actualType.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        
        self.lineNumber = wx.StaticText(self.panel_2, -1, "\n\n\n\n\n\n\n\n\n\n\nNumero da linha:" + str(lineNumber))
        self.lineNumber.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.mensage = wx.StaticText(self.panel_2, -1, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMensagem:\n" + str(failMensage))
        self.mensage.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        self.sizer_8.Add(self.func, 0, 0, 0)
        self.sizer_8.Add(self.type, 0, 0, 0)
        self.sizer_8.Add(self.status, 0, 0, 0)
        self.sizer_8.Add(self.expected, 0, 0, 0)
        self.sizer_8.Add(self.expectedType, 0, 0, 0)
        self.sizer_8.Add(self.actual, 0, 0, 0)
        self.sizer_8.Add(self.actualType, 0, 0, 0)
        self.sizer_8.Add(self.lineNumber, 0, 0, 0)
        self.sizer_8.Add(self.mensage, 0, 0, 0)
        
        #self.button_1 = wx.Button(self.panel_2, -1, "Sair")
        #self.sizer_8.Add(self.button_1, 0, wx.EXPAND, 0)
        #self.panel_2.SetSizer(self.sizer_8)
        self.panel_2.SetSizer(self.sizer_8)
        
        self.Show()
        pass
    def makeTrueFalseStatistics(self, funcName, condition, lineNumber, name, status, mensage):
        self.sizer_8.Clear(True)
        
        self.func = wx.StaticText(self.panel_2, -1, "Método: " + str(funcName))
        self.func.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.type = wx.StaticText(self.panel_2, -1, "\nTipo: " + str(name))
        self.type.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        if(status == True):
            self.status = wx.StaticText(self.panel_2, -1, "\n\nEstado: Passou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
            self.status.SetForegroundColour((0,128,0))
         
        else:
            self.status = wx.StaticText(self.panel_2, -1, "\n\nEstado: Falhou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
            self.status.SetForegroundColour((255,0,0))
            
        self.condition = wx.StaticText(self.panel_2, -1, "\n\n\nCondição: " + str(condition))
        self.condition.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.lineNumber = wx.StaticText(self.panel_2, -1, "\n\n\n\nNumero da linha: " + str(lineNumber))
        self.lineNumber.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        self.mensage = wx.StaticText(self.panel_2, -1, "\n\n\n\n\n\n\nNumero da linha:\n" + str(mensage))
        self.mensage.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        self.sizer_8.Add(self.func, 0, 0, 0)
        self.sizer_8.Add(self.type, 0, 0, 0)
        self.sizer_8.Add(self.status, 0, 0, 0)
        self.sizer_8.Add(self.condition, 0, 0, 0)
        self.sizer_8.Add(self.lineNumber, 0, 0, 0)
        self.sizer_8.Add(self.mensage, 0, 0, 0)
        
        #self.button_1 = wx.Button(self.panel_2, -1, "Sair")
        #self.sizer_8.Add(self.button_1, 0, wx.EXPAND, 0)
        #self.panel_2.SetSizer(self.sizer_8)
        self.panel_2.SetSizer(self.sizer_8)
        
        self.Show()
        pass
    
    def makeMethodStatistics(self, funcName, status):
        self.sizer_8.Clear(True)
         
        self.func = wx.StaticText(self.panel_2, -1, "Método: " + str(funcName))
        self.func.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        if(status == 0):
            self.status = wx.StaticText(self.panel_2, -1, "\nEstado: Passou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
            self.status.SetForegroundColour((0,128,0))
            
        else:
            self.status = wx.StaticText(self.panel_2, -1, "\nEstado: Falhou")
            self.status.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans")) 
            self.status.SetForegroundColour((255,0,0))
        self.sizer_8.Add(self.status, 0, 0, 0)
        self.sizer_8.Add(self.func, 0, 0, 0)
        
        self.panel_2.SetSizer(self.sizer_8)
        
        self.Show()
        
        pass
        
    def removeTreeElements(self):
        self.tree.DeleteAllItems()
        pass
    
    def getTree(self):
        return self.tree
        pass
    def getAllCheckBox(self):
        return self.listMethods_checkBoxs
        pass
    def getAllMethodsCheckBox(self):
        return self.all_metodos_box
        pass
    def setMethodsList(self, listMethods, check_Method, start_test, selChanged, exitEvent):
        
        self.listMethods = listMethods
        self.__do_layout(check_Method)
        self.Bind(wx.EVT_BUTTON, start_test, self.button_5)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, selChanged, self.tree)
        self.Bind(wx.EVT_BUTTON, exitEvent, self.button_6)
        self.Bind(wx.EVT_CLOSE, exitEvent, self)
        
        pass
    

    def checkAll_Methods(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        
        for checkBox in self.listMethods_checkBoxs:
            if(self.all_metodos_box.IsChecked() == True):
                checkBox.SetValue(True)
            else:
                checkBox.SetValue(False)
                
        event.Skip()

    



    def exitProgram(self, event):  # wxGlade: PyUnitiABCP.<event_handler>
        print "Event handler `exitProgram' not implemented"
        event.Skip()

# end of class PyUnitiABCP
'''if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = PyUnitiABCP(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()'''
