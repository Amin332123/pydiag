


def  ecrire_liste_courses(chemin, articles): 
    with open(chemin, 'w') as file  : 
        for i in range(len(articles)) : 
            file.write(f"{articles[i]}\n")
            
# articles = ["pommes", "lait", "pain"]
# ecrire_liste_courses("courses.txt", articles)
    


def ajouter_article(chemin, article) : 
    with open(chemin , 'a') as file : 
        file.write(f"{article}\n")


# ajouter_article("courses.txt", "oeufs")



def lire_fichier(chemin) : 
    with open(chemin , 'r') as file : 
        content = file.readlines()

    return content

# print(lire_fichier("courses.txt"))





def compter_lignes(chemin) : 
    with open(chemin , 'r') as file : 
        number_of_lines = len(file.readlines())
        
    return f"Nombre de lignes : {number_of_lines}"


# print(compter_lignes("courses.txt"))




### bloc 3 is finish , these next ones just for documentation .


def read_binary(chemin) : 
    with open(chemin , 'rb') as file: 
        return file
    

# print(read_binary("courses.txt"))