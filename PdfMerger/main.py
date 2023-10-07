#help from :- https://python-bloggers.com/2022/04/merging-pdfs-with-python-2/
import PyPDF2

Pdffiles = ['unit-1 CSS.pdf', 'unit-2 CSS.pdf']
PdfMerger = PyPDF2.PdfMerger()
for filename in Pdffiles:
    PdfFile = open(filename,'rb')
    PdfFileReader = PyPDF2.PdfReader(PdfFile)
    PdfMerger.append(PdfFileReader)
PdfFile.close()
PdfMerger.write("unit-1&2 CSS.pdf")