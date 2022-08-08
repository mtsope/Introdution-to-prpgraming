def greatTheUser():
    "This function grets the user"
    print("Hello")
    print ("Welcome to our funtion")


greatTheUser()
greatTheUser()
print ("This is more stuff being printed outside  the funcion")
greatTheUser()


print("*************Parameterized Funtion*****************")

def gretPerson(name):
    "This funcion greats the user by name"
    print ("Greetings"), name
    
personName = input("What is your name?")
gretPerson(personName)

def addThese(a,b):
    "Add 2 number together"
    c = a + b
    print(c)

addThese(10.2, 1)


family = ["Michela", "Maguigas", "Doroteia", "Ayla"]

def printFirst(myList):
    print (myList[0])


printFirst(family)   


print("*************Return Funtion*****************")