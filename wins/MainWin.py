# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class MainWin
###########################################################################

class MainWin ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"合并PDF"), pos = wx.DefaultPosition, size = wx.Size( 697,512 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainBox = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.addFile = wx.Button( self, wx.ID_ANY, _(u"添加文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.addFile, 0, wx.ALL|wx.EXPAND, 5 )

        self.clearFiles = wx.Button( self, wx.ID_ANY, _(u"清空列表"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.clearFiles, 0, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( bSizer7, 0, wx.EXPAND, 5 )

        fileList = wx.BoxSizer( wx.VERTICAL )

        self.fileList = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
        self.fileIndex = self.fileList.AppendTextColumn( _(u"序号"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.fileName = self.fileList.AppendTextColumn( _(u"文件名"), wx.dataview.DATAVIEW_CELL_INERT, 500, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.choose = self.fileList.AppendToggleColumn( _(u"选择"), wx.dataview.DATAVIEW_CELL_ACTIVATABLE, -1, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        fileList.Add( self.fileList, 1, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( fileList, 1, wx.EXPAND, 5 )

        output = wx.BoxSizer( wx.HORIZONTAL )

        self.outFileText = wx.StaticText( self, wx.ID_ANY, _(u"选择输出文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.outFileText.Wrap( -1 )

        output.Add( self.outFileText, 0, wx.ALL|wx.EXPAND, 5 )

        self.outFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"选择输出文件"), _(u"PDF files (*.pdf)|*.pdf"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
        output.Add( self.outFile, 1, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( output, 0, wx.EXPAND, 5 )

        self.bRun = wx.Button( self, wx.ID_ANY, _(u"合并"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MainBox.Add( self.bRun, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( MainBox )
        self.Layout()
        self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.addFile.Bind( wx.EVT_BUTTON, self.add )
        self.clearFiles.Bind( wx.EVT_BUTTON, self.clearfiles )
        self.bRun.Bind( wx.EVT_BUTTON, self.run )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def add( self, event ):
        event.Skip()

    def clearfiles( self, event ):
        event.Skip()

    def run( self, event ):
        event.Skip()


