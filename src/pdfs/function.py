
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


def getMetaData(file: str):

    with open(file, "rb") as f:

        reader = PdfReader(f)
        metadata = reader.metadata
        text = reader
        

    return metadata, text


if __name__ == "__main__":

    metadata, text = getMetaData("C:/Users/QHD/Desktop/2024年上半年英语六级笔试准考证.pdf")

    print(text)

    for item in metadata:
       
       print(item, ':', metadata[item])


