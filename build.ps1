


# 编译
.\env\python.exe -m PyInstaller -F -w --add-data '.\static\*;.' '.\main.py'

# 清除缓存
del .\main.spec
del .\build\ -recurse

# 执行
.\dist\main.exe


