import sys, os
sys.path.append(os.getcwd())

import wx
import src.wins as wins
import src.panels as panels

class MainFrame(wins.TestWin):
    
    def __init__(self, parent):
        wins.TestWin.__init__(self, parent) 

        p1 = panels.WelcomeFrame(self.funList)
        p2 = panels.MergeFrame(self.funList, self.statusBar)
        p3 = panels.SplitFrame(self.funList)
        p4 = panels.ToPNGPFrame(self.funList)

        self.funList.AddPage(p1, '首    页', True, imageId=0)
        self.funList.AddPage(p2, 'PDF 合并', imageId=1)
        self.funList.AddPage(p3, 'PDF 拆分', imageId=2)
        self.funList.AddPage(p4, 'PDF转PNG', imageId=3)


'''
主运行入口
'''
if __name__=='__main__':
    app = wx.App(False) 
    frame = MainFrame(None) 
    frame.Show(True) 
    app.MainLoop() 




