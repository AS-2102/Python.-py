s = input("give a sentence : ")

s1 = s.lower()

a = s1.count("a")
e = s1.count("e")
i = s1.count("i")
u = s1.count("u")
o = s1.count("o")

print(f"No of Vowels : {a+e+i+u+o}")

