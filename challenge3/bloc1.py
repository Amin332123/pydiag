

def division_securisee(a, b) :  
    try : 
        return a / b
    except ZeroDivisionError : 
        return 'Erreur : division par zero impossible.'


# print(division_securisee(10, 2))
# print(division_securisee(10, 0))



def convertir_entier(valeur) : 
    
    try : 
        return int(valeur)
    except ValueError : 
        return f'Erreur : "{valeur}" nest pas un entier valide'
    
# print(convertir_entier("42"))
# print(convertir_entier("abc"))



notes = [12, 15, 9]

def acceder_element(notes , index) :  
    try : 
        return notes[index]
    
    except IndexError : 
        return f'Erreur : index {index} hors limites (taille de la liste : {len(notes)}).'




# print(acceder_element(notes, 1))
# print(acceder_element(notes, 10))



eleve = {"nom": "Sara", "age": 20}

def acceder_cle(dictionnaire, cle) : 
    
    try : 
        return dictionnaire[cle]
    
    except KeyError : 
        return f'Erreur : la cle "{cle}" n’existe pas' 


# print(acceder_cle(eleve, "nom"))
# print(acceder_cle(eleve, "email"))

def traiter_valeur(x) :
    try : 
        int(x)
    except ValueError: 
         print(f"Erreur : '{x}' nest pas convertible.")
    else : 
        print(f"Conversion reussie : {x}")
        
    finally : 
        print("Traitement termine") 
        


# traiter_valeur("8")
# traiter_valeur("x")



