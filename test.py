print("Yo")
print("What's your name?")
name=input().lower()
if name=="nick" or "nicolas":
    print("EWWWW!!!")
else:
    print("nice")

print("")

print("How tall are you in centimetres")
height=input()
int_height=int(height)
if int_height>=180:
    print("Cap")
elif int_height<=180:
    print("Ha, gottem. So short. Samir is taller for now.")

print("")

print("How old are you?")
age=input()
int_age=int(age)
if int_age>=17:
    print("SOOOOOOOOO OOOOOOOLDDD!!!")
elif int_age<=16:
    print("SOOOOOOOOO YOOOOOUNG!!")