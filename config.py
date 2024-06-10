import sys
from os.path import join, dirname
if getattr(sys, 'frozen', None):
    # EXE 执行时静态文件路径
    basedir = sys._MEIPASS
else:
    # 开发时静态文件路径
    basedir = join(dirname(__file__), 'static')   

