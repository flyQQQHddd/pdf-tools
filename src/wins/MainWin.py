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
import wx.html

import gettext
_ = gettext.gettext

###########################################################################
## Class MainWin
###########################################################################

class MainWin ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"合并PDF"), pos = wx.DefaultPosition, size = wx.Size( 766,512 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
        self.pageCount = self.fileList.AppendTextColumn( _(u"页数"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER, wx.dataview.DATAVIEW_COL_RESIZABLE )
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
        self.addFile.Bind( wx.EVT_BUTTON, self.OnAddFile )
        self.clearFiles.Bind( wx.EVT_BUTTON, self.OnClearFiles )
        self.fileList.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.fileListOnDataViewListCtrlItemContextMenu, id = wx.ID_ANY )
        self.fileList.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.fileListOnDataViewListCtrlSelectionChanged, id = wx.ID_ANY )
        self.bRun.Bind( wx.EVT_BUTTON, self.OnRun )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnAddFile( self, event ):
        event.Skip()

    def OnClearFiles( self, event ):
        event.Skip()

    def fileListOnDataViewListCtrlItemContextMenu( self, event ):
        event.Skip()

    def fileListOnDataViewListCtrlSelectionChanged( self, event ):
        event.Skip()

    def OnRun( self, event ):
        event.Skip()


###########################################################################
## Class TestWin
###########################################################################

class TestWin ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"集成界面（测试）"), pos = wx.DefaultPosition, size = wx.Size( 879,571 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainBox = wx.BoxSizer( wx.VERTICAL )

        self.funList = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

        MainBox.Add( self.funList, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( MainBox )
        self.Layout()
        self.menubar = wx.MenuBar( 0 )
        self.setting = wx.Menu()
        self.menubar.Append( self.setting, _(u"首选项") )

        self.about = wx.Menu()
        self.menubar.Append( self.about, _(u"关于") )

        self.SetMenuBar( self.menubar )

        self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class WelcomePanel
###########################################################################

class WelcomePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 766,512 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gSizer1 = wx.GridSizer( 3, 3, 0, 0 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer1.Add( self.m_staticText4, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"welcome!"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class MergePanel
###########################################################################

class MergePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 766,512 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        MainBox = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.addFile = wx.Button( self, wx.ID_ANY, _(u"添加文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.addFile, 0, wx.ALL|wx.EXPAND, 5 )

        self.clearFiles = wx.Button( self, wx.ID_ANY, _(u"清空列表"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.clearFiles, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.black = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12.Add( self.black, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer7.Add( bSizer12, 1, wx.EXPAND, 5 )

        self.UpItem = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.UpItem.SetBitmap( wx.Bitmap( u"source/up.bmp", wx.BITMAP_TYPE_ANY ) )
        bSizer7.Add( self.UpItem, 0, wx.ALL|wx.EXPAND, 5 )

        self.DownItem = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.DownItem.SetBitmap( wx.Bitmap( u"source/down.bmp", wx.BITMAP_TYPE_ANY ) )
        bSizer7.Add( self.DownItem, 0, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( bSizer7, 0, wx.EXPAND, 5 )

        fileList1 = wx.BoxSizer( wx.VERTICAL )

        self.fileList = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
        self.fileIndex = self.fileList.AppendTextColumn( _(u"序号"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.fileName = self.fileList.AppendTextColumn( _(u"文件名"), wx.dataview.DATAVIEW_CELL_INERT, 500, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.pageCount = self.fileList.AppendTextColumn( _(u"页数"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.choose = self.fileList.AppendToggleColumn( _(u"选择"), wx.dataview.DATAVIEW_CELL_ACTIVATABLE, -1, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        fileList1.Add( self.fileList, 1, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( fileList1, 1, wx.EXPAND, 5 )

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

        # Connect Events
        self.addFile.Bind( wx.EVT_BUTTON, self.OnAddFile )
        self.clearFiles.Bind( wx.EVT_BUTTON, self.OnClearFiles )
        self.UpItem.Bind( wx.EVT_BUTTON, self.OnItemUp )
        self.DownItem.Bind( wx.EVT_BUTTON, self.OnItemDown )
        self.fileList.Bind( wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.fileListOnDataViewListCtrlItemContextMenu, id = wx.ID_ANY )
        self.fileList.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.fileListOnDataViewListCtrlSelectionChanged, id = wx.ID_ANY )
        self.bRun.Bind( wx.EVT_BUTTON, self.OnRun )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnAddFile( self, event ):
        event.Skip()

    def OnClearFiles( self, event ):
        event.Skip()

    def OnItemUp( self, event ):
        event.Skip()

    def OnItemDown( self, event ):
        event.Skip()

    def fileListOnDataViewListCtrlItemContextMenu( self, event ):
        event.Skip()

    def fileListOnDataViewListCtrlSelectionChanged( self, event ):
        event.Skip()

    def OnRun( self, event ):
        event.Skip()


###########################################################################
## Class SplitPanel
###########################################################################

class SplitPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 766,512 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        MainBox = wx.BoxSizer( wx.VERTICAL )


        self.SetSizer( MainBox )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class ToPNGPanel
###########################################################################

class ToPNGPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 766,512 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        MainBox = wx.BoxSizer( wx.VERTICAL )

        self.m_htmlWin1 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        MainBox.Add( self.m_htmlWin1, 0, wx.ALL, 5 )


        self.SetSizer( MainBox )
        self.Layout()

    def __del__( self ):
        pass


