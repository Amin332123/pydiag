
#atelier_python = ["Ali", "Sara", "Lina", "Karim"]
#atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]


def intersection(a , b) : 
    a , b = set(a) , set(b)
    return a & b

def union(a, b):
    a, b = set(a), set(b) 
    return a | b 

def symetric_defference(a, b) : 
    a, b = set(a), set(b) 
    return a - b
    
"""
    
print(f"nscrits aux deux ateliers : {intersection(atelier_python , atelier_java)}")
print(f"Inscrits a au moins un atelier : {union(atelier_python , atelier_java)}")
print(f"Uniquement Python : {symetric_defference(atelier_python , atelier_java)}")
"""

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]
def a_des_doublons(liste) : 
    converted_list = set(liste) 
    
    return len(liste) != len(converted_list)
        
""" 

print(a_des_doublons(liste_1))
print(a_des_doublons(liste_2))

"""
"""
tags_articles = [
["python", "web", "api"],
["python", "data"],
["web", "css"],
]
"""


def unique_set(liste) : 
    final_result = set()
    for element in liste : 
        final_result.update(element)

    return final_result 


# print(unique_set(tags_articles))



# coordonnees = {[1, 2], [3, 4]}


coordonnees = {(1, 2), (3, 4)}
print(coordonnees)