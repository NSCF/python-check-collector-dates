from extractDataFromSpecify import *

birthYear = 1950
deathYear = 2000
results = extractDatesFromDB()

def checkYear():

  records = []
  for result in results:
    if result[1] != None:
      if result[1] <= birthYear or result[1] >= deathYear:
        print("Year collected:", result[1])
        records.append(result[0])
  return records

checkYear()

