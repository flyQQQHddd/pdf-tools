
import wx
import src.wins as wins

class WelcomeFrame(wins.WelcomePanel):
    '''
    继承 WelcomePanel
    '''
    def __init__(self, parent):
        wins.WelcomePanel.__init__(self, parent) 


        self.richText.BeginBold()
        self.richText.BeginFontSize(20)
        self.richText.WriteText("欢迎使用 PDF 工具箱")
        self.richText.EndFontSize()
        self.richText.EndBold()
        
        self.richText.Newline()

        self.richText.BeginBold()
        self.richText.BeginFontSize(10)
        self.richText.BeginItalic()
        self.richText.WriteText("by Qu Haodong")
        self.richText.EndItalic()
        self.richText.EndFontSize()
        self.richText.EndBold()

        self.richText.Newline()
        self.richText.Newline()
        self.richText.Newline()
        self.richText.Newline()
        self.richText.Newline()
        self.richText.Newline()

        self.richText.BeginURL("https://github.com/flyQQQHddd/pdf-tools")
        self.richText.WriteText("GitHub 项目链接")
        self.richText.EndURL()



