

from operator import length_hint


names = ["Michela", "Tsope", "Sergio", "Sitoe", "Sara"]
gpas = [1.2, 23.23, 31.1, 3.34, 55]

print(names[0])
print(names[3])
print(gpas[0])

#Adicioar novo item no array
names.append("Gildo")
print(names[5])

#Eliminar um item no array
del names[3]


for name in names:
    print(name)

total = 0
for score in gpas:
    total = total + score

print("The Avarege GPA is", (total/len(gpas)))
