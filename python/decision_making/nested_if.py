weather = input("weather : ")
time = input("time of the day :")
if weather == "sunny":
    
    if time == "day":
        print("let's stay here.")

    elif time == "afternoon":
        print("it's dinner time.")

    else :
        print("stay inside the home.")

if weather == "rainy":

    if time == "day":
        print("stay inside the home.")

    elif time == "afternoon":
        print("it's dinner time.")

    else :
        print("stay inside the home.")