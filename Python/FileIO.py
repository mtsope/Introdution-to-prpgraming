
from turtle import position


print("*****************wright")
myFile = open("family.txt", "wb")
myFile.write("Michela\n")
myFile.write("Gildo\n")
myFile.write("Bela\n")
myFile.write("Zu\n")
myFile.write("Silas\n")

print("Just wrote the file: ", myFile.name)
print("Opened file in mode", myFile.mode)
myFile.close()


print("*****************Ready")
myFileR = open("poem.txt", "r+")
poem = myFileR.read(5)
position = myFileR.tell()
print("Position of the file pointer", position)
print(poem)
myFileR.close()