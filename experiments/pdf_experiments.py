import PyPDF2
from PyPDF2 import PdfFileReader

class PDFReader:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename+".pdf", 'rb')
        self.pdf = PdfFileReader(self.file)

    def printBookDetails(self):
        print("Details of the book")
        print("Number of pages:", self.pdf.getNumPages())
        print("Title:", self.pdf.getDocumentInfo().title)
        print("Author:", self.pdf.getDocumentInfo().author)

    def printPage(self, pageNo):
        print("Reading Page ", pageNo)
        page = self.pdf.getPage(pageNo)
        print(page.extractText())

    def printOutline(self):
        print("Book Outline")
        for heading in self.pdf.getOutlines():
           if type(heading) is not list:
               print(dict(heading).get('/Title'))


p = PDFReader('automate-it')
p.printBookDetails()
p.printPage(1)
p.printOutline()
