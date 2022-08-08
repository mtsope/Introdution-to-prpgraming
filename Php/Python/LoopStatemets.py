from re import L


print("************ While******************")

i = 0
while i < 11:
    print (i)
    i = i + 1 

print("******************************")

x = 50
while x > 0:
    print (x)
    x = x - 1 


print("**************For****************")


for letter in "Learn to program":
    print("Letter", letter)

print("******************************")
bands = {"Januaty", "February", "March", "April"}
for band in bands:
    print (band)



print("**************Break****************")
for letter in "Happy Bhirthday":
     if letter == "":
         break
     print ("Letter ", letter)


print("**************Continue****************")
for letter in "Happy Bhirthday":
     if letter == "":
         continue
     print ("Letter ", letter)


print("******************************")
y = 0
while y <  100:
    print(y)
    if i == 15:
        break
    y = y + 1


