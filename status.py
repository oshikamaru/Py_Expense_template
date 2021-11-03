import csv

def print_status():
    # Read the expense_report.csv
    with open('expense_report.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          if (row[0] != 'amount'):
              print(row[3] + ' owes ' + row[0] + '€ to ' + row[2])
    return True;