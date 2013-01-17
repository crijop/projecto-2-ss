#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Jan 17 12:17:44 2013

import wx

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.ficheiro = wx.Menu()
        self.verfirificarErros = wx.MenuItem(self.ficheiro, wx.NewId(), "Verificar Erros", "", wx.ITEM_NORMAL)
        self.ficheiro.AppendItem(self.verfirificarErros)
        self.ficheiro.AppendSeparator()
        self.sair = wx.MenuItem(self.ficheiro, wx.NewId(), "Sair", "", wx.ITEM_NORMAL)
        self.ficheiro.AppendItem(self.sair)
        self.frame_1_menubar.Append(self.ficheiro, "Ficheiro")
        self.ajuda = wx.Menu()
        self.acercaAplic = wx.MenuItem(self.ajuda, wx.NewId(), u"Acerca Aplicação", "", wx.ITEM_NORMAL)
        self.ajuda.AppendItem(self.acercaAplic)
        self.frame_1_menubar.Append(self.ajuda, "Ajuda")
        wxglade_tmp_menu = wx.Menu()
        self.frame_1_menubar.Append(wxglade_tmp_menu, "item")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.list_box_1 = wx.ListBox(self, -1, choices=[])

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.evt_verif_erros, self.verfirificarErros)
        self.Bind(wx.EVT_MENU, self.evt_sair, self.sair)
        self.Bind(wx.EVT_MENU, self.evt_acercAplica, self.acercaAplic)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.list_box_1.SetMinSize((1366, 708))
        self.list_box_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.list_box_1, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
    

    def evt_sair(self, event): # wxGlade: MyFrame.<event_handler>
        if wx.MessageBox("Deseja sair do programa?", "Confirmar", wx.YES_NO) == wx.YES :
            exit(0)
            pass
        event.Skip()

    def evt_verif_erros(self, event): # wxGlade: MyFrame.<event_handler>
        menssagem = "OLA"
        self.list_box_1.AppendAndEnsureVisible(menssagem)
        event.Skip()

    def evt_acercAplica(self, event): # wxGlade: MyFrame.<event_handler>
        msg = "Esta interface é utilizada para utilizadores que programam \
na linguagem de programação Python. \n\
Tem o objectivo de Mostrar os erros que o utilizador tem no código, \
quando este utiliza a programação conduzida por testes.\n\n\n \
Interface Elaborada por:\n Carlos Palma Nº 5608\n António Baião Nº 5604"
        wx.MessageBox(msg, 'Acerca Programação Conduzida por Testes',
            wx.OK | wx.ICON_INFORMATION)
        event.Skip()

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
