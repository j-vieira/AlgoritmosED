print("Categoria dos Nadadores")

idade = int(input("Coloque a idade do nadador: "))

if 4>=idade>=0: 
    print("Categoria Baby")
if 10>=idade>=5: 
    print("Categoria Infantil")
if 17>=idade>=11: 
    print("Categoria Juvenil")
if idade>=18:
    print("Categoria Master")