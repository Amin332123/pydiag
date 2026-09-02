etudiants = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "Lina", "notes": [6, 8, 5]},
]

resultats = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
"Lina": {"moyenne": 8.7, "mention": "Insuffisant"},
"Nadia": {"moyenne": 13.5, "mention": "Bien"},
}


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



def construire_resultats(etudiants) : 
    final_result = {}
    for student in etudiants : 
        avg = calculer_moyenne(student['notes'])
        final_result[student['nom']] = {"moyenne": round(avg , 2), "mention": appreciation(avg)}
       
    return final_result 





def classer_par_moyenne(resultats) : 
    final_result = dict (
        sorted(resultats.items() , key=lambda item: item[1]["moyenne"] , reverse=True)
    )
    return final_result
    
        
 
def etudiants_en_echec(resultats) : 
    final_result: list = []
    for key , value in resultats.items() : 
        if value["moyenne"] < 10 : 
            new_tuple:tuple = (key , value["moyenne"])
            final_result.append(new_tuple)

    return  final_result 



def regrouper_par_mention(resultats) : 
    final_result:dict = {} 
    for key , value in resultats.items() : 
       
        if value["mention"] not in final_result : 
            final_result[value["mention"]] = []
        final_result[value["mention"]].append(key)
        
    return final_result



noms = ["Karim", "Sara", "Lina", "Karim"]
# Attention, il y a des doublons ! 
def detect_double_names(names) :
    
    for i , name_i in enumerate(names[::-1])  : 
        for j , name_j in enumerate(names[1::]): 
            if name_i == name_j : 
                return "Attention, il y a des doublons ! "
                
                
        
        

groupe_a = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
"ahmed": {"moyenne": 12.0, "mention": "Bien"}
}
groupe_b = {
"Karim": {"moyenne": 15.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
"Karim": {"moyenne": 1.0, "mention": "Bien"},
"ahmed": {"moyenne": 12.0, "mention": "Bien"}
}

def fusion(group_a , group_b) : 
    final_result = {} 
    for key_a , value_a in group_a.items() : 
        for key_b , value_b in group_b.items() : 
            if key_a in group_b : 
                if key_a not in final_result : 
                    final_result[key_a] = [value_a]
       
                if key_a == key_b :              
                   final_result[key_a].append(value_b)  
            else : 
                if key_a not in final_result : 
                    final_result[key_a] = value_a
                else : 
                    final_result[key_a].append(value_b)
                   
    for key , value in group_b.items() : 
        if key not in final_result :
              final_result[key] = value
    
    return final_result
print(fusion(groupe_a , groupe_b))
    