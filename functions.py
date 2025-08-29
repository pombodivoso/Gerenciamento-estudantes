

#-------------------------------------------------------------------
Students = []
Disciplines = []
Teachers = []
Classes = []
Registrations = []

#-------------------------------------------------------------------
def ShowAll(listOption): #A function to show the list informations
    if not listOption:
        print("Lista vazia!")
    else:
        print("===================================================================================================")
        for i in listOption:
            print(i)
            print("===================================================================================================")

def Include(addedData, listOption): #A function to include something new on the list
    listOption.append(addedData)

def UpdateStudent(searchInfo): #A function to update all the students information
    for dic in Students:
        if dic["Id"] == searchInfo:
            dic["Nome"] = input("Digite o novo nome: ")
            dic["Data de Nascimento"] = input("Digite a nova data de nascimento(dia/mes/ano): ")
            dic["CPF"] = input("Digite o novo CPF (sem traços/pontos): ")
            break
        else:
            print("Não encontrado!")
            
def UpdateTeacher(searchInfo): #A function to update all the teachers information 
    for dic in Teachers:
        if dic["Id"] == searchInfo:
            dic["Nome"] = input("Digite o novo nome: ")
            dic["Data de Nascimento"] = input("Digite a nova data de nascimento(dia/mes/ano): ")
            dic["CPF"] = input("Digite o novo CPF (sem traços/pontos): ")
            dic["Especialização"] = input("Digite a nova matéria de especialização: ")
            break
        else:
            print("Não encontrado!")
            
def UpdateDisciplines(searchInfo): #A function to update all the discipline information 
    for dic in Disciplines:
        if dic["Id"] == searchInfo:
            dic["Nome da Disciplina"] = input("Digite o novo nome: ")
            dic["Carga horária"] = input("Digite a nova carga horária: ")
            
def UpdateClasses(searchInfo): #A function to update all the classes information 
    for dic in Classes:
        if dic["Id"] == searchInfo:
            dic["Tempo de Aula"] = input("Digite o novo tempo de aula: ")
            dic["Numero de alunos"] = input("Digite o novo número de alunos: ")
            dic["Sala de Aula"] = input("Digite a nova sala de aula: ")
            dic["Materia"] = input("Digite a nova matéria: ")
            
def UpdateRegistration(searchInfo): #A function to update all the Registration information 
    for dic in Registrations:
        if dic["Id"] == searchInfo:
            StudentId = input("Digite o ID novo do estudante:")
            ClassId = input("Digite o ID novo da turma:")
            TeacherId = input("Digite o ID novo do professor:")
            for Studentdics in Students:
                for Classdics in Classes:
                    for Teacherdics in Teachers:
                        if Studentdics["Id"] == StudentId and Classdics["Id"] == ClassId and Teacherdics["Id"] == TeacherId:
                            dic["Id do aluno"] = StudentId
                            dic["Id da turma"] = ClassId
                            dic["Id do professor"] = TeacherId

        

def Exclude(listOption, searchInfo):  #A function to delete something on the list 
    for dic in listOption:
        if dic["Id"] == searchInfo:
            listOption.remove(dic)
        else:
            print("Item não encontrado!")

#-------------------------- STUDENT --------------------------------
def MenuOptions(ChosenOption, NextChosenOption):  
    if ChosenOption == 1:
        if NextChosenOption == 1:
            StudentId = input("Digite o ID de 5 dígitos: ")
            Name = input("Digite o nome do estudante: ")
            NumberStudents = input("Digite sua data de nascimento (dia/mes/ano): ")
            Id = input("Digite o CPF do estudante (sem pontos/traços): ")
            dictionary = {
                "Id" : StudentId,
                "Nome" : Name,
                "Data de Nascimento" : NumberStudents,
                "CPF" : Id
            }
            Include(dictionary, Students)
        elif NextChosenOption == 2:
            ShowAll(Students)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Students)
            search = input("Digite seu ID: ")
            UpdateStudent(search)
        elif NextChosenOption == 4:
            ShowAll(Students)
            search = input("Digite Id do aluno que deseja excluir: ")
            Exclude(Students, search)
               
#-------------------------- DISCIPLINE --------------------------------
    elif ChosenOption == 2:
        if NextChosenOption == 1:
            DisciplineId = input("Digite o ID de 5 dígitos: ")
            Name = input("Digite o nome da disciplina: ")
            Workload = input("Digite a carga horária: ")
            dictionary = {
                "Id" : DisciplineId,
                "Nome da Disciplina" : Name,
                "Carga horária" : Workload
            }
            Include(dictionary, Disciplines)
        elif NextChosenOption == 2:
            ShowAll(Disciplines)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Disciplines)
            search = input("Digite o ID: ")
            UpdateDisciplines(search)
        elif NextChosenOption == 4:
            ShowAll(Disciplines)
            search = input("Digite o Id da disciplina que deseja excluir: ")
            Exclude(Disciplines, search)

#-------------------------- TEACHER --------------------------------
    elif ChosenOption == 3:
        if NextChosenOption == 1:
            ClassId = input("Digite o ID de 5 dígitos: ")
            Name = input("Digite o nome do professor: ")
            NumberStudents = input("Digite sua data de nascimento (dia/mes/ano): ")
            Id = input("Digite o CPF do professor (sem pontos/traços): ")
            MainCourse = input("Digite sua matéria de especialização: ")
            dictionary = {
                "Id" : ClassId,
                "Nome" : Name,
                "Data de Nascimento" : NumberStudents,
                "CPF" : Id,
                "Especialização" : MainCourse
            }
            Include(dictionary, Teachers)
        elif NextChosenOption == 2:
            ShowAll(Teachers)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Teachers)
            search = input("Digite seu ID: ")
            UpdateTeacher(search)
        elif NextChosenOption == 4:
            ShowAll(Teachers)
            search = input("Digite o Id do prefessor deseja excluir: ")
            Exclude(Teachers, search)

#-------------------------- CLASSES --------------------------------
    elif ChosenOption == 4:
        if NextChosenOption == 1:
            ClassId = input("Digite o ID de 5 dígitos: ")
            NumberStudents = int(input("Digite o número de alunos: "))
            ClassTime = input("Digite o tempo de aula: ")
            MainCourse = input("Digite sua matéria de especialização: ")
            Classroom = input("Digite o número da sala de aula: ")
            dictionary = {
                "Id" : ClassId,
                "Tempo de Aula" : ClassTime,
                "Numero de alunos" : NumberStudents,
                "Materia" : MainCourse,
                "Sala de Aula" : Classroom
            }
            Include(dictionary, Classes)
        elif NextChosenOption == 2:
            ShowAll(Classes)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Classes)
            search = input("Digite seu ID: ")
            UpdateClasses(search)
        elif NextChosenOption == 4:
            ShowAll(Classes)
            search = input("Digite o Id da turma que deseja excluir: ")
            Exclude(Classes, search)

#-------------------------- REGISTRATION --------------------------------
    elif ChosenOption == 5:
        if NextChosenOption == 1:
            RegistrationId = input("Digite o ID de 5 dígitos: ")
            ShowAll(Students)
            StudentId = input("Digite o ID do estudante: ")
            ShowAll(Classes)
            ClassId = input("Digite o ID da turma: ")
            ShowAll(Teachers)
            TeacherId = input("Digite o ID do professor: ")
            dictionary = {
                "Id" : RegistrationId,
                "Id do aluno" : StudentId,
                "Id da turma" : ClassId,
                "Id do professor" : TeacherId
            }
            Include(dictionary, Registrations)
        elif NextChosenOption == 2:
            ShowAll(Registrations)
            input("\nPressione ENTER para continuar...")
        elif NextChosenOption == 3:
            ShowAll(Registrations)
            search = input("Digite seu ID: ")
            UpdateRegistration(search)
        elif NextChosenOption == 4:
            ShowAll(Registrations)
            search = input("Digite o Id da matrícula que deseja excluir: ")
            Exclude(Registrations, search)
