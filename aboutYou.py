"""
 input your AGE in years
 input your HIGHT in meters 
 input you MASS in kg

 ---
 code made in September 2023
"""



#######
# Age #
#######
age = int(input())
year = 2023
year_birthday = year - age
if age <110:
    if age >= 18:
        print ("You born in:", str(year_birthday))
        if age >= 60:
            print ("You are old")
    elif age < 18:
        print ("Not there yet")
elif age >= 110:
    print ("You are dead")
#########

print ("")

#########
# Hight #
#########
if age <110:
    hight = float(input())
    if hight > 1.0:
        if hight < 1.8:
            print ("You have a normal hight")
        elif hight <= 1.8:
            print ("Dont hit your head")
            print ("Tall one")
    elif hight <= 1.0:
        print ("You are a dwarf")
###########

    print ("")

#######
# BMI #
#######

    mass = float(input())
    bmi = int((mass / (hight * hight)))
    print("Your BMI is:", f"{bmi:.{1}f}")
    print ("")
    print ("You are:")
    if bmi < 17.0:
            print ("the skinny one")
    elif ((bmi >= 17.0) and (bmi < 18.5)):
            print ("underweight my friend")
    elif ((bmi >= 18.5) and (bmi < 24.9)):
            print ("the normal one")
    elif ((bmi >= 24.9) and (bmi < 29.9)):
            print ("little overweight, but who is counting?")
    elif ((bmi >= 29.9) and (bmi < 34.9)):
            print ("starting to get obese :/")
            print ("time to hit the gym")
    elif ((bmi >= 34.9) and (bmi < 39.9)):
            print ("on a severe one")
            print ("call backup and lets burn this sh*")
    elif bmi > 39.9:
            print ("on the heavyweight division")
            print ("no one will mess with you")
