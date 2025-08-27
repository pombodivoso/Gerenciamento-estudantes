import datetime #importing the library to deal with dates

#-------------------------------------------------------------------
def ShowAll(listOption): #A function to show the list informations
    if not listOption:
        print("Lista vazia!")
    else:
        print("=================================")
        for i in listOption:
            print(i)
            print("=================================")

def Include(addedData, listOption): #A function to include something new on the list
    listOption.append(addedData)

def Update(listOption, searchInfo, newInfo): #A function to update something on the list 
    for listIdx, info in enumerate(listOption):
        if info == searchInfo:
            listOption[listIdx] = newInfo
            return
    print("Item não encontrado!")

def Exclude(listOption, searchInfo):  #A function to delete something on the list 
    if searchInfo in listOption:
        listOption.remove(searchInfo)
    else:
        print("Item não encontrado!")

#-------------------------------------------------------------------
def MenuOptions(ChosenOption, NextChosenOption):  
    if ChosenOption == 1:
        if NextChosenOption == 1:
            NewData = input("Digite o nome do estudante: ")
            Include(NewData, Students)
        elif NextChosenOption == 2:
            ShowAll(Students)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Students)
            search = input("Digite o que você deseja alterar: ")
            newInf = input("Digite a nova opção: ")
            Update(Students, search, newInf)
        elif NextChosenOption == 4:
            ShowAll(Students)
            search = input("Digite o que você deseja excluir: ")
            Exclude(Students, search)

    elif ChosenOption == 2:
        if NextChosenOption == 1:
            NewData = input("Digite a nova disciplina: ")
            Include(NewData, Disciplines)
        elif NextChosenOption == 2:
            ShowAll(Disciplines)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Disciplines)
            search = input("Digite o que você deseja alterar: ")
            newInf = input("Digite a nova opção: ")
            Update(Disciplines, search, newInf)
        elif NextChosenOption == 4:
            ShowAll(Disciplines)
            search = input("Digite o que você deseja excluir: ")
            Exclude(Disciplines, search)

    elif ChosenOption == 3:
        if NextChosenOption == 1:
            NewData = input("Digite o novo professor: ")
            Include(NewData, Teachers)
        elif NextChosenOption == 2:
            ShowAll(Teachers)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Teachers)
            search = input("Digite o que você deseja alterar: ")
            newInf = input("Digite a nova opção: ")
            Update(Teachers, search, newInf)
        elif NextChosenOption == 4:
            ShowAll(Teachers)
            search = input("Digite o que você deseja excluir: ")
            Exclude(Teachers, search)

    elif ChosenOption == 4:
        if NextChosenOption == 1:
            NewData = input("Digite a nova turma: ")
            Include(NewData, Classes)
        elif NextChosenOption == 2:
            ShowAll(Classes)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Classes)
            search = input("Digite o que você deseja alterar: ")
            newInf = input("Digite a nova opção: ")
            Update(Classes, search, newInf)
        elif NextChosenOption == 4:
            ShowAll(Classes)
            search = input("Digite o que você deseja excluir: ")
            Exclude(Classes, search)

    elif ChosenOption == 5:
        if NextChosenOption == 1:
            NewData = input("Digite a nova matrícula: ")
            Include(NewData, Registrations)
        elif NextChosenOption == 2:
            ShowAll(Registrations)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Registrations)
            search = input("Digite o que você deseja alterar: ")
            newInf = input("Digite a nova opção: ")
            Update(Registrations, search, newInf)
        elif NextChosenOption == 4:
            ShowAll(Registrations)
            search = input("Digite o que você deseja excluir: ")
            Exclude(Registrations, search)
