
'''
基于 PyPDF 构建的功能函数

Documation: https://pypdf.readthedocs.io/en/stable/
'''

from pypdf import PdfWriter, PdfReader

def merge(files: list, output: str, pages: list = None) -> None :

    merger = PdfWriter()
    for file in files:

        input = open(file, "rb")
        if pages is not None:
            merger.append(fileobj=input, pages=(0, 3))
        
        else:
            merger.append(fileobj=input)
        
        input.close()

    output = open(output, "wb")
    merger.write(output)

    # Close file descriptors
    merger.close()
    output.close()


def getPageCount(file: str) -> int:

    with open(file, "rb") as f:
        reader = PdfReader(f)
        pageCount = reader.get_num_pages()

    return pageCount

