

gpas = {
    "Mark Lassoff"  : 3.23,
    "Fred Smith"    : 1.23,
    "Ana Matavel"   : 2.32,
    "Sara Tivane"   : 3.34,
    "Tina Roda"     : 4.12,
    "Quino"         : 1.22
 }


print("The GPA is: ", (gpas["Mark Lassoff"]))
print("The GPA is: ", (gpas["Mark Lassoff"]))

print('***************************')
gpas["Ana Matavel"] = 2.75
gpas["Sara Tivane"] = 2.90

del gpas["Fred Smith"]

if gpas.has_key("Mark Lassoff" ):
    print("Mark is present")

if gpas.has_key("Tina Roda" ):
    print("Tina is present")
else:
    print("Fred is gone")

print(gpas.keys())
print(gpas.values())

print(len(gpas))

