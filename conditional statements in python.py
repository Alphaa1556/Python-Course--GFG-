age=20
if age>=18:
    print("Eligible to vote.")

age=15
if age<=12:
    print("Travel for free")
else:
    print("Pay for Ticket")

age=17
if age<=12:
    print("child")
elif age<=19:
    print("teenager")
elif age<=35:
    print("Young adult")
else:
    print("adult")

age=70
is_member=True

if age>=60:
    if is_member:
        print("30% senior discount")
    else:
        print("20% senior discount")
else:
    print("Not eligible for discount")

age=20
s="adult" if age>=18 else "minor"
print(s)

number=2
match number:
    case 1:
        print("one")
    case 2|3:
        print("two or three")
    case _:
        print("Other number")
    
