
from __future__ import with_statement


with open("life-expectancy.csv") as life_expetancy_file:
    for line in life_expetancy_file:
        line = line.strip()
        parts = line.split(",")

        life_expetancy = parts[3]
        year = parts[2]
        country = parts[0]


year_of_intrest = int(input("Enter year of intrest: "))


