from datetime import *
import time
import names

n = 0
concats = []

todayis = date.today() 
day_of_birth = todayis.strftime("%d-%m-%Y")

while n < 20:
    name = names.get_first_name()
    surname = names.get_last_name()
    concat = name, surname, day_of_birth
    concat = ', '.join(concat)
    concats.append(str(concat))

    n = n + 1

concats = '\n'.join(concats)
print(concats)

file_time = time.strftime("%d-%m-%Y-%H;%M;%S")

with open("C:\SSIS\Integration_Services_Project3\person.txt", 'w') as file:
    file.write(concats)
