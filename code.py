while True:
    #List of the chooseable activeties
    # for age 
    age_min = 4
    age_max = 18
    camp_leader_age = 14

    #Activtys can be changed here
    name_input = ""
    age_input = ""
    camp_input =""
    meal_input =""
    shuttle_input =""
    end_input=""

    # Activity list
    activities = [
        ("1", "Cultural immersion   ", 5, "easy     ", 800),
        ("2", "Kayaking & pancakes  ", 3, "moderate ", 400),
        ("3", "Mountain biking      ", 4, "difficult", 900)
    ]

    print(" num   activity               days   diff        cost")
    for act in activities:
        print(f" {act[0]}     {act[1]}      {act[2]}      {act[3]}      ${act[4]}")

    #store the name
    name_input =""
    while name_input == "" or name_input.isalpha() == False:
        name_input = input("what is your name? ")
        if name_input  == "" or name_input.isalpha() == False:
            print("you need to enter your name no numbers or symbols")

    #camper age
    camper_age =""
    while camper_age == "" or camper_age.isdigit() == False :
        camper_age = input("what is your age? ")
        if camper_age  == "" or camper_age.isdigit() == False:
            print("you need to enter your age")

    # says that you're the right age
    if int(camper_age) > age_min and int(camper_age) < age_max:
        print(f"{camper_age} you are the right age to go to camp")

    # too young or too old
    if int(camper_age) <= age_min:
        print(f"{camper_age} you are too young to go to camp")
        exit()

    if int(camper_age) >= age_max:
        print(f"{camper_age} you are too old to go to camp")
        exit()

    # camp leader
    if int(camper_age) > camp_leader_age and int(camper_age) < age_max:
        print(f"{camper_age} you are qulifyed to be a camp leader")
  
    #camp choice
    activity_number = ""
    while True:
        activity_number = input("Which camp do you want to go to? (1, 2, or 3): ")

        if activity_number.isdigit() and activity_number in ["1", "2", "3"]:
            activity_number = int(activity_number)
            break
        else:
            print(" you must enter 1,2 or 3 using only digits")

    if activity_number == 1:
        print("Camp 1 costs $800")
        base_cost = 800
    elif activity_number == 2:
        print("Camp 2 costs $400")
        base_cost = 400
    elif activity_number == 3:
        print("Camp 3 costs $900")
        base_cost = 900

    # MEAL VALIDATION
    meal_input = ""
    while meal_input.lower() not in ["standard", "vegetarian", "vegan"]:
        meal_input = input("What meals do you want: standard, vegetarian or vegan? ")
        if meal_input.lower() not in ["standard", "vegetarian", "vegan"]:
            print("please choose standard, vegetarian, or vegan.")

    # SHUTTLE VALIDATION
    shuttle = ""
    while shuttle.lower() not in ["yes", "no"]:
        shuttle = input("Do you need the shuttle bus - extra $80? (yes or no): ")
        if shuttle.lower() not in ["yes", "no"]:
            print("please choose yes or no. ")

    # SHUTTLE COST 
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
            pass

    elif shuttle.lower() == "no":
        added_number = base_cost

    else:
        pass

    #FINAL MESSAGE
    print(f"\nThank you, {name_input}! You are {camper_age} years old and you chose Camp {activity_number}.")
    print(f"You selected a {meal_input} meal plan and your shuttle option was '{shuttle}'.")
    print(f"Your total cost for camp is ${added_number}.")

    # FINAL CONFIRMATION VALIDATION 
    end_input = ""
    while end_input.lower() not in ["yes", "no"]:
        end_input = input("Is this correct (yes or no): ")
        if end_input.lower() not in ["yes", "no"]:
            print(" please enter yes or no.")

    if end_input.lower() == "yes":
        print("Have a good time at camp.")
        break
    else:
        print("Okay, let's try again.\n")

