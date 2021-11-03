from PyInquirer import prompt
import csv

with open('users.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    dataList = list(reader)
    data = []
    for row in dataList :
        if (row[0] != 'name'):
            data.append(row[0])

    expense_questions = [
        {
            "type":"input",
            "name":"amount",
            "message":"Rentrer le montant de la dépense: ",
        },
        {
            "type":"input",
            "name":"label",
            "message":"Rentrer un motif: ",
        },
        {
            "type":"list",
            "name":"spender",
            "message":"Rentrer le nom de la personne qui dépensé: ",
            "choices": data,
        },
    ]

    involved_questions = [
        {
            "type":"list",
            "name":"involved_user",
            "message":"Rentre le(s) nom(s) des personnes impliquées dans la transaction: ",
            "choices": data,
        },
        {
            "type":"list",
            "name":"involved_again",
            "message":"D'autres personnes sont-elles impliquées dans la transactions ?",
            "choices": ['Oui', 'Non'],
        },
    ]


# This function create a new expense, asking for its amount,label and spender and store it in expense_report.csv
def new_expense(*args):
    infos = prompt(expense_questions)
    
    # Store all the users involved in an array
    involved_users = []

    # Loop while there is still involved people
    involved = prompt(involved_questions)    
    while (involved['involved_again'] == 'Oui'):
        involved_users.append(involved['involved_user'])
        involved = prompt(involved_questions)    
    involved_users.append(involved['involved_user'])

   # Read the file to store the number of line
    with open('expense_report.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      row_count = sum(1 for row in reader)

    with open('expense_report.csv', 'a+') as csvfile:
        fieldnames = ['amount', 'label', 'spender', 'involved']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # If the number of rows is 0, add the header
        if (row_count == 0):
            writer.writeheader()
        amount = int(infos["amount"])
        for elm in involved_users:
            infos["involved"] = elm
            infos["amount"] = amount / len(involved_users)
            writer.writerow(infos)

    print("Dépense ajoutée !")
    return True


