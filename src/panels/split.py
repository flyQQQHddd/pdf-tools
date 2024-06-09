

import wx
import src.wins as wins
from src.pdfs import function as F
from os.path import join


class RangeListModel(wx.dataview.PyDataViewModel):

    def __init__(self):

        super(RangeListModel, self).__init__()
        self.data = []
        self.items = []

        self.columnType = {
            0: 'int',
            1: 'string',
            2: 'string',
            3: 'int',
            4: 'bool'
        }
    
    def IsContainer(self, item):

        return False
    
    def GetChildren(self, parent, children):

        for row in range(len(self.data)):
            children.append(self.ObjectToItem(self.data[row]))
        
        return len(self.data)
    
    def GetColumnType(self, col):

        return self.columnType[col]

    def GetValue(self, item, col):

        return self.ItemToObject(item)[col]

    def SetValue(self, value, item, col):

        index = int(self.ItemToObject(item)[0]) - 1
        self.data[index][col] = value

        item = self.ObjectToItem(self.data[index])
        self.items[index] = item
        self.ItemChanged(item)
        return True
    
    def GetParent(self, item):

        return wx.dataview.NullDataViewItem
    
    def DeleteAllItems(self):

        self.data = []
        for item in self.items:
            self.ItemDeleted(wx.dataview.NullDataViewItem, item)

    def GetItemCount(self):

        return len(self.data)

    def AppendItem(self, data):

        self.data.append(data)
        item = self.ObjectToItem(data)
        self.items.append(item)

        self.ItemAdded(
            wx.dataview.NullDataViewItem,
            item)


class SplitFrame(wins.SplitPanel):
    '''
    继承 SplitPanel
    '''
    def __init__(self, parent, statusBar): 
        wins.SplitPanel.__init__(self, parent) 

        self.statusBar: wx.StatusBar = statusBar

        self.model = RangeListModel()
        self.rangeList.AssociateModel(self.model)

    def OnAddRange(self, event):
        '''
        "添加文件" 按钮的回调函数
        '''

        try: 
            pageCount = F.getPageCount(self.inFile.GetPath())

            self.model.AppendItem([
                f'{self.model.GetItemCount() + 1}', 
                f'1-{pageCount}',
                f'split{self.model.GetItemCount() + 1}',
                f'1/{pageCount}',
                True])
            
        except:
            errorBox = wx.MessageDialog(
                self, 
                "输入文件为空！", 
                "错误信息提示", 
                wx.YES_DEFAULT | wx.ICON_QUESTION)

            if errorBox.ShowModal() == wx.ID_YES:
                errorBox.Destroy()


    def OnClearRanges(self, event):
        '''
        "清空列表" 按钮的回调函数
        '''
        
        self.model.DeleteAllItems()


    def rangeListOnDataViewListCtrlSelectionChanged(self, event):
        '''
        获取被选择的对象，记录被选择对象的行数
        将在 rangeListOnDataViewListCtrlItemContextMenu 之前被执行
        '''

        selection = self.rangeList.GetSelection()
        self.selected = self.rangeList.ItemToRow(selection)


    def OnRun(self, event):
        '''
        "分割" 按钮的回调函数
        '''

        # 获取输出文件目录
        output = self.outDir.GetPath()

        if output == '':            
            
            errorBox = wx.MessageDialog(
                self, 
                "输出目录为空！", 
                "错误信息提示", 
                wx.YES_DEFAULT | wx.ICON_QUESTION)

            if errorBox.ShowModal() == wx.ID_YES:
                errorBox.Destroy()

            return

        # 获取被选择的所有输入文件
        files = []
        ranges = []
        for item in self.model.data:
            choose = item[4]
            if choose:
                files.append(item[2])
                ranges.append(item[1])
            
        if len(files) == 0:

            errorBox = wx.MessageDialog(
                self, 
                "输出范围列表为空！", 
                "错误信息提示", 
                wx.YES_DEFAULT | wx.ICON_QUESTION)

            if errorBox.ShowModal() == wx.ID_YES:
                errorBox.Destroy()

            return
        
        # 连接输出目录
        files = [join(output, file) + '.pdf' for  file in files]


        # 处理 ranges 字符串
        # TODO: 处理 ranges 字符串

        print('OnRun')
        self.statusBar.SetLabelText(f'拆分成功！【{output}】')