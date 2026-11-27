x,y,z = input("give three numbers:").split(" ")

num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1 == num2 and num2 == num3 :
    print("all are equal")

elif num1 > num2 and num1 > num3 :
    print(f"greater num : {num1}")
elif num2 > num1 and num2 > num3 :
   print(f"greater num : {num2}")

elif num3 > num1 and num3 > num2 :
    print(f"greater num : {num3}")

elif num1 >= num2  :
    if num1 > num3 :
         print(f"greater num : {num1}")

    else : 
        print(f"greater num : {num3}")

elif num2 >= num3 :
    if num2 > num1 :
        print(f"greater num : {num2}")
    else : 
        print(f"greater num : {num1}")

 

elif num3 >= num1 :
    if num3 > num2 :
        print(f"greater num : {num3}")

    else : 
        print(f"greater num : {num1}")

