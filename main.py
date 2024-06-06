
import sys, os
sys.path.append(os.getcwd())

import wx
import wins
from src import function as F

class MainFrame(wins.MainWin):

    def __init__(self, parent): 
        wins.MainWin.__init__(self, parent) 

    def add(self, event):

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

                self.fileList.AppendItem([
                    str(self.fileList.GetItemCount() + 1), 
                    file,
                    True])
                

    def clearfiles(self, event):

        self.fileList.DeleteAllItems()


    def run(self, event): 


        files = []
        for i in range(self.fileList.GetItemCount()):

            file = self.fileList.GetTextValue(i, 1)
            choose = self.fileList.GetTextValue(i, 2)

            if choose == '1':
                files.append(file)
            else:
                pass

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

        F.merge(files, output)

        self.statusBar: wx.StatusBar

        self.statusBar.SetLabelText(f'合并成功！【{output}】')


        
app = wx.App(False) 
frame = MainFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 

