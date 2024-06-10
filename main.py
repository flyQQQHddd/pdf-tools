import sys, os
sys.path.append(os.getcwd())

import wx
import src.wins as wins
import src.panels as panels
import config
from os.path import join

class MainFrame(wins.MainWin):
    
    def __init__(self, parent):
        wins.MainWin.__init__(self, parent)

        self.SetStatusText("欢迎使用 PDF 工具箱！")

        p1 = panels.WelcomeFrame(self.funList)
        p2 = panels.MergeFrame(self.funList, self.statusBar)
        p3 = panels.SplitFrame(self.funList, self.statusBar)
        p4 = panels.ToPNGPFrame(self.funList)

        # 新增一个ImageList对象，存在四个Bitmap对象进去
        wx.InitAllImageHandlers()
        imagelist = wx.ImageList(52, 52, False, 1)
        imagelist.Add(wx.Bitmap(join(config.basedir, '首页.png')))
        imagelist.Add(wx.Bitmap(join(config.basedir, '合并.png')))
        imagelist.Add(wx.Bitmap(join(config.basedir, '拆分.png')))
        imagelist.Add(wx.Bitmap(join(config.basedir, '转换.png')))
        self.funList.AssignImageList(imagelist)

        self.funList.AddPage(p1, '首    页', imageId=0)
        self.funList.AddPage(p2, '合    并', imageId=1)
        self.funList.AddPage(p3, '拆    分', imageId=2)
        self.funList.AddPage(p4, '转    换', imageId=3)

'''
主运行入口
'''
if __name__=='__main__':
    app = wx.App(False) 
    frame = MainFrame(None) 
    frame.Show(True) 
    app.MainLoop() 




