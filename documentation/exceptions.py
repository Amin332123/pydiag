# writing a simple code for getting used to the syntax . 
"""
try : 
    user_input = int(input('enter a number : '))
    final_result = 10 / user_input
    print(f"final : {final_result}")
    
except ZeroDivisionError :  
    print('u can not devide by 0 . ')

except ValueError : 
    print('enter a valid number')
    
else : 
    print('it was good . ')
    
finally : 
    print('code is excuted and now finished ')
    
"""


# i will raise an exception without try and except : 

"""
user_input = int(input('enter something : '))  
if user_input <= 0  :
    raise ValueError('you must enter a positive number')


"""


# use my custom exception using a class . 



"""
class My_exception(Exception): 
    pass



try : 
    raise My_exception("Test exception")

except My_exception as e: 
    print(e)
    
"""
