import csv

fh = open("100-contacts.csv", "r")

reader = csv.DictReader(fh)

for row in reader:
    print(str(reader.line_num), row['first_name'], row['last_name'])

fh.close()
