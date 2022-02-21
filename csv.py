import csv

def passwd_to_csv(file_passwd, file_csv):
    f = open(file_passwd)
    g = open(file_csv)
    with f as passwd, g as output:
        input_file = csv.reader(passwd, delimiter = ':')
        output_file = csv.writer(output, delimiter = '\t')
    for row in input_file:
        if len(row) > 1: 
            output_file.writerow(row[0], row[2])
