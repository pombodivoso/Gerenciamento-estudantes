import json

STUDENTS_FILE = "Students.json"
DISCIPLINES_FILE = "Disciplines.json"
TEACHERS_FILE = "Teachers.json"
CLASSES_FILE = "Classes.json"
REGISTRATIONS_FILE = "Registrations.json"

#-------------------------------------------------------------------
def SaveFile(listOption, fileOption):
    with open(fileOption, 'w', encoding='utf-8') as file:
        json.dump(listOption, file, ensure_ascii=False, indent=4)

def ReadFile(fileOption):
    try:
        with open(fileOption, 'r', encoding='utf-8') as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
#------------------------------------------------------------------

Students = ReadFile(STUDENTS_FILE)
Disciplines = ReadFile(DISCIPLINES_FILE)
Teachers = ReadFile(TEACHERS_FILE)
Classes = ReadFile(CLASSES_FILE)
Registrations = ReadFile(REGISTRATIONS_FILE)

#-------------------------------------------------------------------

def _save_for_list(listOption):
    if listOption is Students:
        SaveFile(Students, STUDENTS_FILE)
    elif listOption is Disciplines:
        SaveFile(Disciplines, DISCIPLINES_FILE)
    elif listOption is Teachers:
        SaveFile(Teachers, TEACHERS_FILE)
    elif listOption is Classes:
        SaveFile(Classes, CLASSES_FILE)
    elif listOption is Registrations:
        SaveFile(Registrations, REGISTRATIONS_FILE)

def ShowAll(fileOption): #A function to show the list informations
    if not fileOption:
        print("Lista vazia!")
    else:
        print("===================================================================================================")
        for i in fileOption:
            print(i)
            print("===================================================================================================")

def Include(addedData, fileOption): #A function to include something new on the list
    fileOption.append(addedData)
    _save_for_list(fileOption)

def UpdateStudent(searchInfo): #A function to update all the students information
    found = False
    for dic in Students:
        if dic.get("Id") == searchInfo:
            dic["Nome"] = input("Digite o novo nome: ")
            dic["Data de Nascimento"] = input("Digite a nova data de nascimento(dia/mes/ano): ")
            dic["CPF"] = input("Digite o novo CPF (sem traços/pontos): ")
            found = True
            _save_for_list(Students) 
            break
    if not found:
        print("Não encontrado!")
            
def UpdateTeacher(searchInfo): #A function to update all the teachers information 
    found = False
    for dic in Teachers:
        if dic["Id"] == searchInfo:
            dic["Nome"] = input("Digite o novo nome: ")
            dic["Data de Nascimento"] = input("Digite a nova data de nascimento(dia/mes/ano): ")
            dic["CPF"] = input("Digite o novo CPF (sem traços/pontos): ")
            dic["Especialização"] = input("Digite a nova matéria de especialização: ")
            found = True
            _save_for_list(Teachers)
            break
    if not found:
        print("Não encontrado!")
            
def UpdateDisciplines(searchInfo): #A function to update all the discipline information 
    found = False
    for dic in Disciplines:
        if dic["Id"] == searchInfo:
            dic["Nome da Disciplina"] = input("Digite o novo nome: ")
            dic["Carga horária"] = input("Digite a nova carga horária: ")
            found = True
            _save_for_list(Disciplines) 
            break
    if not found:
        print("Não encontrado!")
            
def UpdateClasses(searchInfo): #A function to update all the classes information 
    found = False
    for dic in Classes:
        if dic["Id"] == searchInfo:
            dic["Tempo de Aula"] = input("Digite o novo tempo de aula: ")
            dic["Numero de alunos"] = input("Digite o novo número de alunos: ")
            dic["Sala de Aula"] = input("Digite a nova sala de aula: ")
            dic["Materia"] = input("Digite a nova matéria: ")
            found = True
            _save_for_list(Classes) 
            break
    if not found:
        print("Não encontrado!")
            
def UpdateRegistration(searchInfo): #A function to update all the Registration information 
    found = False
    for dic in Registrations:
        if dic.get("Id") == searchInfo:
            StudentId = input("Digite o ID novo do estudante:")
            ClassId = input("Digite o ID novo da turma:")
            TeacherId = input("Digite o ID novo do professor:")
            student_exists = any(s.get("Id") == StudentId for s in Students)
            class_exists = any(c.get("Id") == ClassId for c in Classes)
            teacher_exists = any(t.get("Id") == TeacherId for t in Teachers)
            if student_exists and class_exists and teacher_exists:
                dic["Id do aluno"] = StudentId
                dic["Id da turma"] = ClassId
                dic["Id do professor"] = TeacherId
                found = True
                _save_for_list(Registrations) 
            else:
                print("Aluno, turma ou professor não encontrado!")
            break
    if not found:
        print("Matrícula não encontrada!")

        

def Exclude(listOption, searchInfo):  #A function to delete something on the list 
    found = False
    for dic in listOption[:]:
        if dic.get("Id") == searchInfo:
            listOption.remove(dic)
            _save_for_list(listOption)
            found = True
            break
    if not found:
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
