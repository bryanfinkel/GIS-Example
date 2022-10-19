
import csv
from django.conf import settings
from .models import Cities

def run():
   with open(str(settings.BASE_DIR / "files/uscities.csv")) as file:
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
