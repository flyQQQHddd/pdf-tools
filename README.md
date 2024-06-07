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

Step2：将解压后的 `Python` 置于 `env `目录下

```
mkdir env
```

Step3：安装 `PIP`

```
./env/python.exe ./get-pip.py
```

Step4：安装第三方包

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

## 功能

- 合并 PDF

## 更新日志

- 2024.6.7：更新合并 PDF 功能，实现了调整输入文件次序的功能
- 2024.6.6：首次提交，实现了合并 PDF 功能

## 链接

https://docs.wxpython.org/index.html

https://pypdf.readthedocs.io/en/stable/