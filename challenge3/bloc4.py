import csv


def lire_fichier_securise(chemin) : 
    try : 
        with open(chemin , 'r') as file : 
            content = file.readlines()
            
    except FileNotFoundError : 
        print('Erreur : le fichier "inexistant.txt" n’existe pas.')
        
    
    else  : 
        print('Contenu du fichier renvoye sous forme de liste de lignes.')
        return content
    
      
      

# lire_fichier_securise("courses.txt")
# lire_fichier_securise("inexistant.txt")




data = [
    ['nom','note'],
    ['Sara',9],
    ['Lina','abc'],
    ['Karim',9],
    ['Ali',14]
    
]

def create_csv_file(chemin , data) : 
    with open(chemin , 'w' , newline='' ) as file : 
        writer = csv.writer(file)
        for i in range(len(data)) : 
            writer.writerow(data[i])
        
        
# create_csv_file("notes.csv" , data )


def calculer_moyenne_csv(chemin) : 
    
        with open(chemin , 'r', newline='') as file : 
           reader = csv.DictReader(file)
           final_result = {
               'moyenne' : 0,
               'number_iterations' : 0
           }
           for person in reader : 
                try : 
                    
                    final_result['moyenne'] += float(person['note'])
               
                    final_result['number_iterations'] += 1
       
                except ValueError : 
                    print(f"Attention : note invalide pour '{person['nom']}' ('{person['note']}'), ligne ignoree.")
    
                
        final_result['moyenne'] /= final_result['number_iterations']
        print(f"Moyenne calculee ({final_result['number_iterations']} notes valides) : {round(final_result['moyenne'], 2)}")
                    
       # print(f"Moyenne calculee ({final_result['number_iterations']} notes valides) : {final_result['moyenne']}")
       

# calculer_moyenne_csv("notes.csv")



stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes = [
"pommes,5",
"bananes,10",
"kiwis,2",
"oranges,abc",
"oranges,5",
]


class StockInsuffisantError(Exception) : 
    pass   

def update_orders(stock , orders) : 
    file = open('journal.txt', 'a')
    
    
    for order in orders : 
        try : 
            order = order.split(',')
            
            if stock[order[0]] < float(order[1]) : 
                raise StockInsuffisantError 
                
            stock[order[0]] -= float(order[1])
            file.write(f"[OK] {order[0]} : -{order[1]} (reste {stock[order[0]]})\n")
    
        except KeyError : 
            file.write(f"[ERREUR] {order[0]} : produit inconnu\n")
        
        except StockInsuffisantError : 
            file.write(f"[ERREUR] {order[0]} : stock insuffisant (demande {order[1]}, dispo {stock[order[0]]})\n")
        
        except ValueError : 
            file.write(f"[ERREUR] {order[0]} : quantite invalide ({order[1]})\n")


update_orders(stock ,commandes_brutes)