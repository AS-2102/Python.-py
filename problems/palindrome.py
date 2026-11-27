s1 = input("give a sentence for palindrome check up :")

s=s1.lower()
s2 = s[::-1]

if s == s2 :
    print("It's a palindrome.")

else:
    print("not a palindrome.")