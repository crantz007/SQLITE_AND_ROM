import sqlite3

# Create or opens database
db = sqlite3.connect('record2s.db')
db.row_factory = sqlite3.Row
cur = db.cursor()

# Menu for choice
menu = ["1 Add ",
        "2 Search",
        "3 Update",
        "4 Delete",
        "5 Quit"]


# Check if the required number is choice for menu

def main():
    choice = 1
    create_table()
    add_record()
    while choice != 5:
        display_menu()
        choice = int(input('Enter a menu choice: '))
        while choice < 0 or choice > 5:
            print('\nEnter a number between 1 and 5 ')
            choice = int(input('Enter a menu choice'))
        get_menu_option(choice)


# Menu choice assigned to numbers
def get_menu_option(choice):
    if choice == 1:
        add_new_record()
    elif choice == 2:
        search_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    else:
        print('This is an invalid choice')


# Create table and check if is exists or not
def create_table():
    cur.execute('create table if not exists record2s(name text, country text, catches int)')


# Add required records
def add_record():
    cur.execute('insert into record2s values("Janne Mustonen","Finland",98)')
    cur.execute('insert into record2s values("Ian Stewart","Canada",94)')
    cur.execute('insert into record2s values("Aaron","Canada",88)')
    cur.execute('insert into record2s values("Chad Taylor","USA",78)')


# Menu Display
def display_menu():
    print('***MENU***')
    for m in menu:
        print('\n' + m)


# Add new records with record holder's informations
def add_new_record():
    # Exception
    try:
        name = input("Enter a record holder: ")
        country = input('Enter the record holder country: ')
        catches = int(input('Enter the record holder catches: '))

        db.execute('insert into record2s values (?,?,?)', (name, country, catches))

    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('Oops! number are required!!')


# Search Records by name
def search_record():
    name = input('Enter the name of the record holder to retrieve: ')
    try:
        # Check if no name is entered
        if name == "":
            query = 'select * from record2s'
            for row in cur.execute(query):
                print('name: ' + row['name'])
                print('country: ' + row['country'])
                print('catches: ' + str(row['catches']))
        # Check record holder's information in db
        else:
            for row in cur.execute('select * from record2s where name =?', (name,)):
                print('name: ' + row['name'])
                print('country: ' + row['country'])
                print('catches: ' + str(row['catches']))
    except sqlite3.Error as e:
        print(e)


# Update record by name and number of catches
def update_record():
    try:
        name = input('Please Enter the name of the record holder to be update: ')
        catches = int(input('Enter amount of catches: '))
        cur.execute('update record2s set catches =? where name =?', (catches, name))
        print('\nrecord updated')
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('Please enter the required input')


# delete record by name
def delete_record():
    name = input('Enter the name of the record holder you wish to delete: ')
    try:
        cur.execute('delete from record2s where name=?', (name,))
        print('\nrecord holder is deleted')
    except sqlite3.Error as e:
        print(e)


main()

db.commit()

db.close()
