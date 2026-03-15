#List of the chooseable activeties
#Activtys can be changed here
name_input = ""
age_input = ""
camp_input =""
meal_input =""
shuttle_input =""
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
    if camper_age  == ""or camper_age.isdigit() == False: print("you need to enter your age")
if int(camper_age) > 4 and int(camper_age) < 18: