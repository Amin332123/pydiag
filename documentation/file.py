import io 
from pathlib import Path 
""" try : 
    file = open('file.txt' , 'x') 
except FileNotFoundError : 
    print('not found')
except FileExistsError : 
    print('file already exists') """
    
# file = open('file.txt' , 'a')

# print(file.readline())
# print(file.readlines())
students_names = ['amine\n', 'mosa\n', 'tyeb\n', 'said\n']
"""for line in file : 
    print(line)"""


"""
try : 
    file.writelines(students_names)
    
except io.UnsupportedOperation : 
    print('u cant write in reading mode')
    file.close()
    
"""
"""
print(Path('documentation'))

with open('file.txt' , 'r') as file : 
    for line in file : 
        print(line)
"""
