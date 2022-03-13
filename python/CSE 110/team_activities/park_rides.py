
# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 35= 36= 36
# Sorry, you may not ride.

# If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

# If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

# If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

# No one under 36 inches may ever ride, either by themselves or with another rider.

# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

# If there are two riders and one of them is at least 18 years old, they may ride together.

age_first_rider = int(input("What is the age of the first rider?"))
height_first_rider = float(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")
age_second_rider = int(input("What is the age of the second rider? "))
height_second_rider = float(input("What is the height of the second rider? "))

if height_first_rider < 36 or height_second_rider < 36:
    ride = False