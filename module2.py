etudiants = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "Lina", "notes": [6, 8, 5]},
]

def calculer_moyenne(notes) : 
    sum_of_elements  = 0
    i = 0 
    for note in notes : 
        i += 1 
        sum_of_elements += note

    return sum_of_elements / i

def appreciation(moyenne) : 
    if moyenne < 10 : 
        return "Insuffisant"
    elif moyenne >= 10 and moyenne < 12 : 
        return "Passable"
    elif moyenne >= 12 and moyenne < 16 : 
        return "Bien"
    elif moyenne >= 16 : 
        return "Tres bien"


def find_best_student(etudiants) : 
    student = etudiants[0]
    for  i_student in etudiants[1::] : 
        if calculer_moyenne(student["notes"]) < calculer_moyenne(i_student["notes"]) : 
            student = i_student

    return student 
        



def find_worst_student(etudiants) : 
    student = etudiants[0]
    for  i_student in etudiants[1::] : 
        if calculer_moyenne(student["notes"]) > calculer_moyenne(i_student["notes"]) : 
            student = i_student
    
    return student 
            


def display_students_with_other_data() : 
    for student in etudiants : 
        avg = calculer_moyenne(student["notes"])
        print(f"{student["nom"]} {avg: >6.2f} {appreciation(avg)}")
    
    print(f"Best student : {find_best_student(etudiants)['nom']}")
    print(f"Worst student : {find_worst_student(etudiants)['nom']}")


def length_calculator(values) : 
    result = 0 
    for value in values :
        result += 1
        
    
    return result

def calculer_moyenne_ponderee(notes , coefficients) :
     final_result = 0 
     sum_of_elements = length_calculator(coefficients)
     for i, note in enumerate(notes) : 
         
         final_result = final_result + (note * coefficients[i])
         
     return final_result / sum_of_elements


def moyenne_groupe(etudiants) :
    final_result = 0
    number_of_students = length_calculator(etudiants)
    for student in etudiants : 
        student_avg =  calculer_moyenne(student["notes"])
        final_result =  final_result + student_avg

    return final_result / number_of_students

display_students_with_other_data()

print(f" moyenne_ponderee : {calculer_moyenne_ponderee([14, 10, 18], [3, 2, 1]): .2f}")


print(f"moyenne_groupe : {moyenne_groupe(etudiants): .2f}")