import csv

def read_csv_file(file):
    file_records = []
    reader = csv.DictReader(open(file,'r'))

    for row in reader:
        file_records.append(dict(row))
    return file_records
print("file_records = " + str(read_csv_file("my_csv.csv")))