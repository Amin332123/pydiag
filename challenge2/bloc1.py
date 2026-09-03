from collections import defaultdict

# notes = [12, 18, 7, 15, 9, 20, 3, 14]
def find_max(list_of_elements) : 
    max = list_of_elements[0]
    for element in  list_of_elements[1::] : 
        if element > max : 
            max = element 
    
    return max 

def find_min(list_of_elements) : 
    min = list_of_elements[0]
    for element in  list_of_elements[1::] : 
        if element < min : 
            min = element 
    
    return min 

# print(f"Note max : {find_max(notes)}")
# print(f"Note min : {find_min(notes)}")





#notes = [8, 14, 6, 17, 11, 20]
#seuil = 12
def notes_au_dessus(notes, seuil) : 
    final_result = [] 
    for note in notes : 
        if note >= seuil : 
            final_result.append(note)
    
    return final_result 


# print(notes_au_dessus(notes, seuil))





fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
def counter(list_of_elements) : 
    final_result = defaultdict(int)
    for element in list_of_elements : 
        final_result[element] += 1
    
    
    return dict(final_result)
     

# print(counter(fruits))




# liste = [1, 2, 3, 4, 5]
def reverse(list_of_elements) : 
    reversed_list = [] 
    i = len(list_of_elements)
    while(i > 0) : 
        reversed_list.append(list_of_elements[i - 1])
        i -= 1
    
    
    return reversed_list


# print(reverse(liste))



#liste_a = [1, 4, 7]
#liste_b = [2, 3, 8, 9]
def fusion(list_a , list_b = []) : 
    final_result = list_a + list_b
    
    if (len(final_result) == 1) : 
        return final_result
    min = final_result[0] 
    for element in final_result[1::] : 
        if element < min : 
            min = element
    
    final_result.pop(final_result.index(min))
    
    return [min] + fusion(final_result) 


#print(fusion(liste_a , liste_b))




nombres = [3, 12, 7, 25, 8, 19, 2]

def power_of_even_numbers(numbers) : 
    final_result = [pow(number, 2) for number in numbers if number % 2 == 0] 
    return final_result 

print(power_of_even_numbers(nombres))