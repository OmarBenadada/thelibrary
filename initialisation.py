import re
def is_right(message,fonction,erroe_message):
    while True:
        value=input(message)
        if fonction(value):
            return value
        else:print(erroe_message)
        
def book_title():
    
    return is_right("Please Enter The Title of the Books  : ",
             lambda x: re.sub(r'\s+','',x).isalpha(),
             "Wrong Input Please Try Again")
    
    
def book_author():
    
    return is_right(f"Please Enter The full name of the Author : ",
             lambda x: re.sub(r'\s+','',x).isalpha(),
             "Wrong Input Please Try Again")
    
def book_year():
    
    return is_right(f"Please Enter The Year : ",
             lambda x: re.sub(r'\s+','',x).isdigit() and -1000<=int(x)<=2025,
             "Wrong Input Please Try Again")
    
def book_genre():
    
    return is_right(f"Please Enter The Genre  : ",
             lambda x: re.sub(r'\s+','',x).isalpha(),
             "Wrong Input Please Try Again")

def book_content():
    
    return is_right(f"Please Enter The content  : ",
             lambda x: re.sub(r'\s+','',x).isalpha(),
             "Wrong Input Please Try Again")


