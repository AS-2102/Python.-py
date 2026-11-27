temp = int(input("give temperature: "))

units = input("give untits in C or F or K :")

u1 = units.lower()

if  u1 == "c" :
    print(f"Temp in farenheit:{(9*temp)/5 + 32}F")
    print(f"Temp in kelvin : {temp + 273}K")

elif  u1 == "f" :
    print(f"Temp in celsius:{((temp - 32)*9)/5}C")
    print(f"Temp in kelvin : {(((temp - 32)*9)/5) + 273}K")

elif  u1 == "k" :
    print(f"Temp in celsius:{temp - 273}C")
    print(f"Temp in farenheit : {((temp - 273)*9)/5 + 32 }F")