"""
Play with PDFs
"""

import PyPDF2

pdf_normal = open("test.pdf", "rb")

pdf_obj = PyPDF2.PdfFileReader(pdf_normal)

print(pdf_obj.numPages)

print(pdf_obj.getPage(0).extractText())

pdf_normal.close()