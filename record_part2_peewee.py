from peewee import *

# Create or opens database
db = SqliteDatabase('records.sqlite')


# storing model in db
class recordman(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} {self.catches} number of catches'


# Ask the database to save changes
db.connect()
# creating tables
db.create_tables([recordman])


# prints  record holder  by catches
def print_table():
    recordHolder = (recordman.select()).order_by(recordman.catches.desc())
    print()
    print('Record Holders for Most Catches')
    print("-" * 33)
    for holder in recordHolder:
        print(holder)
    print()


# adds another record holder
def add_new_record(name, country, catches):
    new_record = recordman(name=name, country=country, catches=catches)
    new_record.save()
    print_table()


# Displays record holder by name
def search_holder(name):
    recordHolder = recordman.get_or_none(recordman.name == name)
    print()
    print(recordHolder)
    print()


# delete record holder by name
def delete_holder(name):
    recordman.delete().where(recordman.name == name).execute()
    print_table()


# updates catches by name
def update_catches(name, catches):
    recordman.update(catches=catches).where(recordman.name == name).execute()
    print_table()


# display menu
def main():
    while True:
        print()
        print('1: Add a new record ')
        print('2: Search for a record ')
        print('3: Update number of catches for a record ')
        print('4: Delete a record ')
        print()

        choice = input('Enter a number between 1 and 5 or Q to quit ')
        # Add record holder to table
        if choice == "1":
            name = str(input("Enter record holder's name: "))
            country = str(input(f"Enter the country {name} is from: "))
            catches = int(input(f"Enter the number of catches {name} got: "))
            add_new_record(name, country, catches)
        # Search for record holder by name
        elif choice == "2":
            name = str(input("Enter record holder's name: "))
            search_holder(name)

        # Update catches  by name
        elif choice == "3":
            name = str(input("Enter record holder's name: "))
            new_catches = int(input("Enter new total number of catches: "))
            update_catches(name, new_catches)

        # Delete record holder by name
        elif choice == "4":
            name = str(input("Enter record holder's name: "))
            delete_holder(name)
        elif choice == "Q" or choice == "q":
            quit()
        else:
            print("This is an invalid choice")


main()
