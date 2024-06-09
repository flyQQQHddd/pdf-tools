# PDF 处理程序

基于 PyPDF 和 wxPython 的可视化 PDF 处理程序

## 开发环境

- Windows 11
- Python 3.8.9-embed-amd64
- PyPDF 4.2.0
- wxPython 4.2.1
- wxFormBuilder 4.2.1-x64

## 快速开始

### 克隆项目

```
git clone https://github.com/flyQQQHddd/pdf-tools.git
cd pdf-tools
```

### 配置Python环境（选择嵌入式版）

Step1：下载 `python-3.8.9-embed-amd64` 并解压

```
https://www.python.org/ftp/python/3.8.9/python-3.8.9-embed-amd64.zip
```

Step2：将解压后的 `Python` 置于 `env` 目录下

```
mkdir env
```

Step3：安装 `PIP`

```
./env/python.exe ./get-pip.py
```

Step4：修改 `Python` 配置

```
# ./env/python38._pth

# Uncomment to run site.main() automatically
import site # 解开这一行的注释（删除`#`）
```

Step5：安装第三方包

```
./env/python.exe -m pip install -r ./requirements.txt
```

### 运行主程序

```
./env/python.exe ./main.py
```

### 打包 EXE 可执行文件

```
./build.ps1
```

### 界面开发（安装 wxFormBuilder ）

https://github.com/wxFormBuilder/wxFormBuilder/releases/download/v4.2.1/wxFormBuilder-4.2.1-x64.exe

## 功能

- 合并 PDF

## 更新日志

- 2024.6.9-2：
    - DEBUG：修改了 2024.6.9 第一列不居中的 BUG (b2024060901) ，官方规定第一列无法设置样式，所以设置一个空白的第一列并隐藏
    - DEBUG：修改了 2024.6.9 '选择'列无法实现应有的功能 BUG (b2024060902) ，需要指定 Column 的属性为 DATAVIEW_CELL_ACTIVATABLE
- 2024.6.9：
    - NEW: 开发了拆分 PDF 页面，在拆分 PDF 页面，使用 PyDataViewModel 和 DataViewCtrl
    - BUG：拆分 PDF 页面的第一列不居中(b2024060901)，'选择'列无法实现应有的功能(b2024060902)
- 2024.6.8：开发了集成界面，为合并 PDF 页面添加了调整文件次序的按钮
- 2024.6.7：更新合并 PDF 功能，实现了调整输入文件次序的功能（右键菜单）
- 2024.6.6：首次提交，实现了合并 PDF 功能


## 链接

https://docs.wxpython.org/index.html

https://pypdf.readthedocs.io/en/stable/