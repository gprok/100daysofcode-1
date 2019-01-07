import openpyxl

workbook = openpyxl.load_workbook('100-contacts.xlsx')
print("Workbook Object:", workbook.sheetnames)

sheet = workbook.active

# iterate over all rows
max_row = sheet.max_row

for i in range(1, max_row+1):

      # get particular cell values
      fname=sheet.cell(row=i,column=1)
      lname=sheet.cell(row=i,column=2)
      # print cell values
      print(fname.value, lname.value)
