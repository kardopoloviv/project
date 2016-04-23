import sys
import csv

def day_value(value, max_value):
    day = 0
    for value in value:
        if value > max_value: 
            day = day + 1
    return day
    

def main(file_name, max_value, file_name_print=None):
    with open(file_name) as h:
        h.readline()
        csv_file = csv.reader(h, delimiter=',')
        value = []
        for row in csv_file:
            x=float((row[5]))
            value.append(x)
    day = day_value(value, max_value)        
    if file_name_print:
        with open(file_name_print, 'w') as f_out:
            f_out.write(str(day))
    print(day)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if len(sys.argv) > 2:
            max_value = sys.argv[2]
            file_name_print = sys.argv[3] if len(sys.argv) > 3 else None
            main(file_name, float(max_value), file_name_print)
        else:
            print("Укажите значение объема торгов")
    else:    
        print("Укажите имя файла")