import sys
import csv
def main(file_name):
    with open('YNDX.csv') as f:
        csv_file = csv.reader(f, delimiter=',')
        for row in csv_file:
            print(row[5])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print('Необходимо указать имя файла')
    