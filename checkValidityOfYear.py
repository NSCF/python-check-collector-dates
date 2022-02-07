from extractDataFromSpecify import *

birthYear = 1950
deathYear = 2000

results = extractDatesFromDB()
# print(results)

def checkYear():
  for result in results:
        if result[1] >= birthYear and result[1] <= deathYear:
            # return True
            print("true")
        elif result[1] <= birthYear or result[1] >= deathYear:
            # return False
            print("false")
        else: 
            # return False
            print("not int")

checkYear()
