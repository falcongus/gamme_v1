import os

a=str(input("Хотите ввести новые значения экрана?(1/0):"))
if a=="1":
    b=str(input("ширина:"))
    c=str(input("высота:"))
    file = open("save", "w")
    file.write(b+"\n")
    file.write(c)
    file.close()