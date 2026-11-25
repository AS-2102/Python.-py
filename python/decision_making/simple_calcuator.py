num1 = int(input("give num1 : "))
num2 = int(input("give num2 : "))
 
b = input("opertor : ")

if b == "+" :
    print(f"num1 + num2  : {num1 + num2}")

elif b == "-" :
    print(f"num1 - num2  : {num1 - num2}")

elif b == "x" :
    print(f"num1 x num2  : {num1 * num2}")

elif b == "%" :
    print(f"num1 / num2  : {num1 / num2}")

else :
    print("invalid.")

