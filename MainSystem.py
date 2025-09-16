import time #importing the time library
import os   #importing the library to clean the terminal
import Functions

ChosenOption = 0

while True: #Infinite loop, so the user decides when they will leave the program
    if ChosenOption == 0:
        os.system("cls")        
        print("==============================") #Initial menu for the system
        print("| SEJA BEM-VINDO AO SISTEMA! |")
        print("==============================")
        print("|      1 - Estudantes        |")
        print("|     2 - Disciplinas        |")
        print("|      3 - Professores       |")
        print("|      4 - Turmas            |")
        print("|      5 - Matrículas        |")
        print("|      6 - Sair              |")
        print("==============================")
        ChosenOption = int(input("Opção desejada: ")) #Gets the input option of the user
        if ChosenOption == 6:
            break
        time.sleep(1) #Waits 1 second before continuing
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
    
    if ChosenOption == 1: 
        os.system("cls") #Cleaning the screen
        print("==============================")
        print("|     BEM-VINDO ESTUDANTE    |")
        print("==============================")
        print("|        1 - Incluir         |")
        print("|        2 - Listar          |")
        print("|        3 - Atualizar       |")
        print("|        4 - Excluir         |")
        print("|    5 - Voltar ao menu      |")
        print("==============================")
        NextChosenOption = int(input("Opção desejada: ")) 
        if NextChosenOption == 5:
            ChosenOption = 0
        else:
            Functions.MenuOptions(ChosenOption, NextChosenOption) #Next Menu
        continue

    elif ChosenOption == 2:
        os.system("cls")
        print("==============================")
        print("|   BEM-VINDO A DISCIPLINA   |")
        print("==============================")
        print("|        1 - Incluir         |")
        print("|        2 - Listar          |")
        print("|        3 - Atualizar       |")
        print("|        4 - Excluir         |")
        print("|    5 - Voltar ao menu      |")
        print("==============================")
        NextChosenOption = int(input("Opção desejada: ")) 
        if NextChosenOption == 5:
            ChosenOption = 0
        else:
            Functions.MenuOptions(ChosenOption, NextChosenOption)
        continue

    elif ChosenOption == 3:
        os.system("cls")
        print("==============================")
        print("|    BEM-VINDO PROFESSOR     |")
        print("==============================")
        print("|        1 - Incluir         |")
        print("|        2 - Listar          |")
        print("|        3 - Atualizar       |")
        print("|        4 - Excluir         |")
        print("|    5 - Voltar ao menu      |")
        print("==============================")
        NextChosenOption = int(input("Opção desejada: ")) 
        if NextChosenOption == 5:
            ChosenOption = 0
        else:
            Functions.MenuOptions(ChosenOption, NextChosenOption)
        continue

    elif ChosenOption == 4:
        os.system("cls")
        print("==============================")
        print("|     BEM-VINDO A TURMA      |")
        print("==============================")
        print("|        1 - Incluir         |")
        print("|        2 - Listar          |")
        print("|        3 - Atualizar       |")
        print("|        4 - Excluir         |")
        print("|    5 - Voltar ao menu      |")
        print("==============================")
        NextChosenOption = int(input("Opção desejada: ")) 
        if NextChosenOption == 5:
            ChosenOption = 0
        else:
            Functions.MenuOptions(ChosenOption, NextChosenOption)
        continue

    elif ChosenOption == 5:
        os.system("cls")
        print("==============================")
        print("|   BEM-VINDO A MATRÍCULA    |")
        print("==============================")
        print("|        1 - Incluir         |")
        print("|        2 - Listar          |")
        print("|        3 - Atualizar       |")
        print("|        4 - Excluir         |")
        print("|    5 - Voltar ao menu      |")
        print("==============================")
        NextChosenOption = int(input("Opção desejada: ")) 
        if NextChosenOption == 5:
            ChosenOption = 0
        else:
            Functions.MenuOptions(ChosenOption, NextChosenOption)
        continue

    else:
        print("Opção inválida! Digite novamente: ")
        ChosenOption = 0

print("Obrigado por utilizar!")
