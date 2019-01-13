import PyPDF2
from PyPDF2 import PdfFileReader

pdf = open("automate-it.pdf", 'rb')
readerObj = PdfFileReader(pdf)


print("Details of the book")
print("Number of pages:", readerObj.getNumPages())
print("Title:", readerObj.getDocumentInfo().title)
print("Author:", readerObj.getDocumentInfo().author)


print("Reading Page 1")
page = readerObj.getPage(1)
print(page.extractText())

print("Book Outline")
for heading in readerObj.getOutlines():
   if type(heading) is not list:
       print(dict(heading).get('/Title'))
