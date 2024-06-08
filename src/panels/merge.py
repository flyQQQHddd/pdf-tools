
import wx
import src.wins as wins
from src.pdfs import function as F

class MergeFrame(wins.MergePanel):

    def __init__(self, parent, statusBar): 
        wins.MergePanel.__init__(self, parent) 

        self.statusBar: wx.StatusBar = statusBar

        # 右键菜单，移动次序
        self.selected: int = -1
        self.file_menu = wx.Menu()
        ItemUp = self.file_menu.Append(0, "上移")
        ItemDown = self.file_menu.Append(1, "下移")
        self.file_menu.Bind(wx.EVT_MENU, self.OnItemUp, ItemUp)
        self.file_menu.Bind(wx.EVT_MENU, self.OnItemDown, ItemDown)


    def OnAddFile(self, event):
        '''
        "添加文件" 按钮的回调函数
        '''

        filesFilter = "PDF files (*.pdf)|*.pdf"
        fileDialog = wx.FileDialog(
            self, 
            message ="选择输入文件", 
            wildcard = filesFilter, 
            style = wx.FD_OPEN|wx.FD_MULTIPLE)

        if fileDialog.ShowModal() !=  wx.ID_OK:

            return
        
        else:

            for file in fileDialog.GetPaths():

                pageCount = F.getPageCount(file)

                self.fileList.AppendItem([
                    str(self.fileList.GetItemCount() + 1), 
                    file,
                    str(pageCount),
                    True])
                

    def OnClearFiles(self, event):
        '''
        "清空列表" 按钮的回调函数
        '''

        self.fileList.DeleteAllItems()


    def fileListOnDataViewListCtrlSelectionChanged(self, event):
        '''
        获取被选择的对象，记录被选择对象的行数
        将在 fileListOnDataViewListCtrlItemContextMenu 之前被执行
        '''

        print('OnSelectionChanged')

        selection = self.fileList.GetSelection()
        self.selected = self.fileList.ItemToRow(selection)

        print(self.selected)


    def fileListOnDataViewListCtrlItemContextMenu(self, event):
        '''
        右键时被触发，弹出菜单
        '''

        if self.selected == -1:
            return

        self.fileList.PopupMenu(self.file_menu)


    def changeTwoItem(self, row1, row2):
        '''
        交换给定两行的值
        '''

        for i in range(1, self.fileList.GetColumnCount()):
            row1Value = self.fileList.GetValue(row1, i)
            row2Value = self.fileList.GetValue(row2, i)

            self.fileList.SetValue(row1Value, row2, i)
            self.fileList.SetValue(row2Value, row1, i)


    def OnItemUp(self, event):
        '''
        将该选项上移一行
        '''

        if self.selected != -1 and self.selected != 0:
            self.changeTwoItem(self.selected, self.selected - 1)
            self.selected = self.selected - 1
            self.fileList.SetCurrentItem(self.fileList.RowToItem(self.selected))

    
    def OnItemDown(self, event):
        '''
        将该选项下移一行
        '''
        
        if self.selected != -1 and self.selected != self.fileList.GetItemCount() - 1:
            self.changeTwoItem(self.selected, self.selected + 1)
            self.selected = self.selected + 1
            self.fileList.SetCurrentItem(self.fileList.RowToItem(self.selected))


    def OnRun(self, event): 
        '''
        "合并" 按钮的回调函数
        '''

        # 获取被选择的所有输入文件
        files = []
        for i in range(self.fileList.GetItemCount()):

            file = self.fileList.GetTextValue(i, 1)
            choose = self.fileList.GetTextValue(i, 3)

            if choose == '1':
                files.append(file)

        
        # 获取输出文件
        output = self.outFile.GetPath()

        if len(files) == 0:

            errorBox = wx.MessageDialog(
                self, 
                "输入文件列表为空！", 
                "错误信息提示", 
                wx.YES_DEFAULT | wx.ICON_QUESTION)

            if errorBox.ShowModal() == wx.ID_YES:
                errorBox.Destroy()

            self.statusBar.SetLabelText(f'ERROR：输入文件列表为空')
            return
        
        if output == '':

            errorBox = wx.MessageDialog(
                self, 
                "输出文件为空！", 
                "错误信息提示", 
                wx.YES_DEFAULT | wx.ICON_QUESTION)

            if errorBox.ShowModal() == wx.ID_YES:
                errorBox.Destroy()

            self.statusBar.SetLabelText(f'ERROR：输出文件为空')
            return

        # 执行合并
        F.merge(files, output)
        self.statusBar.SetLabelText(f'合并成功！【{output}】')