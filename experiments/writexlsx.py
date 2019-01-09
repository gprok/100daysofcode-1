import xlsxwriter

class XlsxCreator:
    """ Creates a xslx file and writes data into it """

    def __init__(self, filename):
        self.filename = filename

    def setData(self, data):
        """ Expects a list of lists (data) representing spreadsheet rows """
        self.data = data

    def createSpreadsheet(self):
        workbook = xlsxwriter.Workbook(self.filename + '.xlsx')
        worksheet = workbook.add_worksheet()
        rowcounter = 0
        for row in self.data:
            colcounter = 0
            for item in row:
                worksheet.write(rowcounter, colcounter, item)
                colcounter += 1
            rowcounter += 1
        workbook.close()


def main():
    data = (
        ['EXPENSE', 'VALUE'],
        ['Rent', 1000],
        ['Gas',   100],
        ['Food',  300],
        ['Gym',    50],
        ['TOTAL', '=SUM(B2:B5)'],
    )
    spreadsheet = XlsxCreator("Expenses01")
    spreadsheet.setData(data)
    spreadsheet.createSpreadsheet()


if __name__== "__main__":
    main()
