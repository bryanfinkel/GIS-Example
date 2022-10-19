
import csv
from django.conf import settings
from .models import Cities
from .models import Airports

print("Please enter the file to be imported using syntax: files/[filename.csv]")
# using input string: files/uscities.csv
# using input string: files/us-airports.csv
VarFileName = input()
print("You've entered ",VarFileName)

# User Interface: Allow User to choose an object to import
WelcomeString ="""
Welcome to the Test Database
Enter 1 to add Cities
Enter 2 to add Airports
Enter 86 to end the program
"""
print(WelcomeString)
UserChoice = input()

# MAIN LOOP: Based on UserChoice, execute respective operations

# BRANCH 1: CITIES
if int(UserChoice) == 1:
    print("You've selected 'Cities' ")
    def run():
       with open(str(settings.BASE_DIR / VarFileName)) as file:
           # with open(str(settings.BASE_DIR / "files/uscities.csv")) as file:  # this line was working prior to my changes
           reader = csv.reader(file)
           next(reader)  # Advance past the header

           for row in reader:
               print(row[1])
               cities = Cities.objects.create(
                   id=row[16],
                   name=row[0],
                   population=row[8],
               )
               cities.save()

# BRANCH 2: AIRPORTS
elif int(UserChoice) == 2:
    print("You've selected 'Airports' ")
    def run():
        with open(str(settings.BASE_DIR / VarFileName)) as file:
            # with open(str(settings.BASE_DIR / "files/uscities.csv")) as file:  # this line was from original Benard code
            reader = csv.reader(file)
            next(reader)  # Advance past the header
            next(reader)  # Advance past the header  # BIF: Duplicated this row because the .csv has TWO header rows above the columns
            print("test")
            for row in reader:
                print(row[1])
                airports = Airports.objects.create(
                    id=row[0],
                    ident=row[1],
                    name=row[3],
                )
                airports.save()
else:
    print ("we arrived at the else statement - must have input the wrong number")