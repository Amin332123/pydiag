from collections import defaultdict
ventes = [
{"produit": "pommes", "montant": 120},
{"produit": "bananes", "montant": 80},
{"produit": "pommes", "montant": 45},
{"produit": "oranges", "montant": 60},
{"produit": "bananes", "montant": 30},
]





def sorting(ventes) : 
    total_per_product = defaultdict(int)
    for product in ventes : 
        total_per_product[product["produit"]] += product["montant"]
        
    max_value =  max(total_per_product.values())
    best_product = ""
    for key , value in total_per_product.items() : 
        if value == max_value : 
            best_product = key
    
    distincted_products = set([product["produit"] for product in ventes ])
    
    return f"""
        Total par produit : {dict(total_per_product)}
        Meilleur produit : {best_product} ({max_value})
        Produits distincts : {distincted_products}
           """
# print(sorting(ventes))



inv1 = {"pommes": 20, "bananes": 15}
inv2 = {"bananes": 10, "kiwis": 5}
# {"pommes": 20, "bananes": 25, "kiwis": 5}

def fusionner_inventaires(inv1, inv2) : 
    
    
    final_result = inv1 
    
    for key ,v in inv2.items() : 
        if key not in inv1 : 
           final_result[key] = 0
        final_result[key] += v
        
    return dict(final_result)


# print(fusionner_inventaires(inv1, inv2))


etudiants = [
{"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
{"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
{"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
]


"""
Moyenne par etudiant :
Ali : 13.0
Sara : 16.33
Lina : 10.0
Matieres enseignees (set) : {"maths", "physique", "svt"}
Notes par matiere :
maths : [14, 18, 9]
physique : [12, 16, 11]
svt : [15]
Meilleure matiere (moyenne globale) : svt (15.0)


"""

# [{"nom": "Ali", "matieres": {"maths": 14, "physique": 12}}]
def final_challege(etudiants) : 
    
    avg_of_students = defaultdict(float)
    fields = []
    fields_with_values = defaultdict(list)
    for student in etudiants :
        student_fields = student["matieres"] 
        i = 0
        for key , v in student_fields.items() :
            fields.append(key)
            fields_with_values[key].append(v)
            avg_of_students[student["nom"]] += v
            i += 1 
        
        avg_of_students[student["nom"]] = round(avg_of_students[student["nom"]] / i, 2)
        
    print("Moyenne par etudiant :")
    for key , value in avg_of_students.items() : 
        print(f"{key} : {value}")
         
    print(f"Matieres enseignees (set) : {set(fields)}")
    print("Notes par matiere :")
    
    for key , value in fields_with_values.items() : 
        print(f"{key} : {value}")
    
    
    max_avg_with_field = max([[k, round(sum(v) / len(v), 2)] for k , v in fields_with_values.items()])
    
    
    print(f"Meilleure matiere (moyenne globale) : {max_avg_with_field[0]} ({max_avg_with_field[1]})")
    
    
    
final_challege(etudiants)
            
            
    
