
def verifier_age(age) : 
    if age < 0 : 
        raise ValueError(f"lage ne peut pas etre negatif ({age})")
       
    print(f"Age valide : {age}")
        
        

#verifier_age(25)
#verifier_age(-3)


def traiter_liste_de_valeurs(liste) : 
    try : 
        for element in liste : 
            int(element)
        
    except ValueError  : 
        
        print(f'Log : valeur "x" invalide, exception relancee.')
        raise
    

#traiter_liste_de_valeurs(["3", "9", "x", "5"]) 
    
    
class StockInsuffisantError(Exception):
    pass

stock = {"pommes": 20, "bananes": 4}
def retirer_stock(stock, produit, quantite) :
    if stock[produit] < quantite : 
        raise StockInsuffisantError(f'stock insuffisant pour "bananes"(demande : {quantite}, disponible : {stock[produit]})')
    
    stock[produit] -= quantite
    print(f'Retrait effectue : {quantite} {produit}.')

retirer_stock(stock, "pommes", 5)
retirer_stock(stock, "bananes", 10)