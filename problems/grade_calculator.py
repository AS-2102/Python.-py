# paper = p
p1 = int(input("marks in maths : "))
p2 = int(input("marks in science : "))
p3 = int(input("marks in english : "))

total_marks = p1 + p2 + p3
avg_marks = total_marks/3

print(f"total_marks : {total_marks}")
print(f"avg_marks : {avg_marks}")

if avg_marks <= 30:
    print("grade : C")
elif avg_marks <= 79:
    print("grade : B")
elif avg_marks <= 100:
    print("grade : A")

else:
    print("grade : p")