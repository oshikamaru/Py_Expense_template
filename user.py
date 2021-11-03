from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

# This function create a new user, asking for its name and store it in users.csv
def add_user():
    infos = prompt(user_questions)

       # Read the file to store the number of line
    with open('users.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      row_count = sum(1 for row in reader)

    with open('users.csv', 'a+') as csvfile:
        fieldnames = ['name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # If the number of rows is 0, add the header
        if (row_count == 0):
            writer.writeheader()
        writer.writerow(infos)

    print("Utilisateur ajouté !")
    return True