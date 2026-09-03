from collections import defaultdict
#stock = {"pommes": 50, "bananes": 30, "oranges": 0}
def vendre(stock, produit, quantite) : 
    if stock[produit] < quantite : 
        return f"Stock insuffisant pour {produit} (disponible : {stock[produit]})"
    
    stock[produit] = stock[produit] - quantite
    
    return f"Vente enregistree : {quantite} {produit}."
    
    
#print(vendre(stock, "pommes", 20))
#print(vendre(stock, "oranges", 5))
#print(stock)


# stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}
def produits_epuises(stock) : 
    final_result = []
    for key , value in stock.items() :
        
        if value == 0 : 
            final_result.append(key)
            
            
    return final_result 


#print(produits_epuises(stock))





"""
commandes = [
{"client": "Ali", "produit": "pommes", "quantite": 5},
{"client": "Sara", "produit": "bananes", "quantite": 10},
{"client": "Ali", "produit": "oranges", "quantite": 2},
] 
"""

def total_par_client(commandes) : 
    final_result = defaultdict(int)
    
    for client in commandes : 
        final_result[client['client']] +=  client['quantite']
    
    
    return dict(final_result)


#print(total_par_client(commandes))


d = {"a": 1, "b": 2, "c": 3}

def Inversion(dictionary) :
    final_result = {v:k for k,v in dictionary.items()}

    return final_result


#print(Inversion(d))




#mots = ["chat", "elephant", "abeille", "riz"]

def calculate_caracters(mots) : 
    final_result = defaultdict(int)
    
    for element in mots :
        final_result[element] = len(element) 
    
    return dict(final_result)


#print(calculate_caracters(mots))




""" entreprise = {
"IT": ["Ali", "Sara", "Omar"],
"RH": ["Lina"],
"Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
} """


def calculate_employees(entreprise) : 
    final_result = defaultdict(str)
        
    for key , value in entreprise.items(): 
        final_result[key] = f"{len(value)} employee(s)"
        
        
    return dict(final_result)


# print(calculate_employees(entreprise))




