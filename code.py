#List of the chooseable activeties
# for age 
age_min = 5
age_max = 17
camp_leader_age = 14
#for camp number and cost
camp_number_min = 1
camp_number_med = 2
camp_number_max = 3
#Activtys can be changed here
name_input = ""
age_input = ""
camp_input =""
meal_input =""
shuttle_input =""
#table for camp options
activity_list = [("1","Cultural immersion",5,"easy ",800)]
activity_list1 = [("2","Kayaking & pancakes",3,"moderate" ,400)]
activity_list2 = [("3","Mountain biking",4,"difficult", 900)]
print("  num   act                days  dif    cost")
print(f"{activity_list}")
print(f"{activity_list1}")
print(f"{activity_list2}")
input("what is your name? ")
camper_age =""
while camper_age == "" or camper_age.isdigit() == False :
    camper_age = input("what is your age? ")
    if camper_age  == "" or camper_age.isdigit() == False:
        print("you need to enter your age")

# says that you're the right age
if int(camper_age) > age_min and int(camper_age) < age_max:
    print(f"{camper_age} you are the right age to go to camp")

# 24 and 25 are to tell if you are too old or too young to go to camp
if int(camper_age) < age_min:
    print(f"{camper_age} you are too young to go to camp")
    exit()   # = stops the program

if int(camper_age) > age_max:
    print(f"{camper_age} you are too old to go to camp")
    exit()   # = stops the program
# if old enough It can tell you that the person is qulifyed to be camp leader
if int(camper_age) > camp_leader_age and int(camper_age) < age_max: print(f"{camper_age} you are qulifyed to be a camp leader")
activity_number = int(input("Which camp do you want to go to? (1, 2, or 3): "))
if activity_number == 1:
    print("Camp 1 costs $800")
elif activity_number == 2:
    print("Camp 2 costs $400")
elif activity_number == 3:
    print("Camp 3 costs $900")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

input("what meals do you want standard, vegeterian of vegan")
shuttle = input("Do you need the shuttle bus - extra $80? (yes or no): ")

if shuttle.lower() == "yes":
    shuttle_input = input("What camp did you pick? 1, 2, or 3: ")

    if shuttle_input == "1":
        added_number = 800 + 80
        print("Total:", added_number)

    elif shuttle_input == "2":
        added_number = 400 + 80
        print("Total:", added_number)

    elif shuttle_input == "3":
        added_number = 900 + 80
        print("Total:", added_number)

    else:
        pass   # invalid camp → print nothing

elif shuttle.lower() == "no":
    pass   # no shuttle → print nothing

else:
    pass   # invalid answer → print nothing

print(f"\nThank you, {name_input}! You are {camper_age} years old and you chose Camp {activity_number}. You selected a {meal_input} meal plan and your shuttle option was '{shuttle}'. Your total cost for camp is ${added_number}. Have a great time!")
