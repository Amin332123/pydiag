nom = input('Enter last name')
prenom = input('Enter first name')
notes = []

 
for i in range(3) : 
    note = input("Enter a note : ") 
    if note.isdigit() :
        notes.append(float(note))
    else  : 
        while (not note.isdigit())  :
            note = input("Enter a note : ") 
            if note.isdigit() : 
                notes.append(float(note))
                break 


def avg(notes) : 
   result = 0 
   i = 0
   for note in notes :  
      result += note 
      i += 1
   return result / i

print(f"{nom} avg {avg(notes): >6.2f}")