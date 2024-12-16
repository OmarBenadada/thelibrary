import pandas as pd
import books
import initialisation
import os

def Exitting(input_func):
    print("If you want to quit at any moment, just type EXITP")
    value = input_func()  
    if value.upper() == 'EXITP':
        print("Exiting...")
        os._exit(0)
    return value

def adding_books(df):

    
    while True:
        
        title=Exitting(initialisation.book_title)
        author=Exitting(initialisation.book_author)
        year=Exitting(initialisation.book_year)
        genre=Exitting(initialisation.book_genre)
        
        if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
            print(f"this book {author} already Exist in the library ")
            continue
   
        else:
            book = books.Books(title=title, author=author, year=year, genre=genre)
            frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
            
            df=pd.concat([df,frame],axis=0,ignore_index=True)
            
            df.to_csv("thelibraryy.csv", index=False)
            
            print("book is added to the library")
            



def lookingfor_books(df):
    
    while True:
        thechoice=input("""
1 -> If Wou Want To See All the books with the same (Title,Author,Year,Genre).
2 -> If You Want To see A Speecific Book By (Title,Author,Year,Genre).
Enter The Choice You want : """)
        match thechoice:
            
            case "1":
                choice=input("""Choose Between the Availble Options 
                        1 -> Looking For Books By Title. 
                        2 -> Looking For Books By Author. 
                        3 -> Looking For Books By Year.
                        4 -> Looking For Books By Genre. 
                        Enter you Number here : """)
                
                match choice:
                    
                    case "1":
                        title=Exitting(initialisation.book_title)
                        the_books_bytitle=df[df["Title"]==title]
                        print(the_books_bytitle)
                    case "2":
                        author=Exitting(initialisation.book_author)
                        the_books_bytitle=df[df["Title"]==author]
                        print(the_books_bytitle)
                    case "3":
                        year=Exitting(initialisation.book_year)
                        the_books_bytitle=df[df["Title"]==year]
                        print(the_books_bytitle)
                    case "4":
                        genre=Exitting(initialisation.book_genre)
                        the_books_bytitle=df[df["Title"]==genre]
                        print(the_books_bytitle)    

            case "2":
                title=Exitting(initialisation.book_title)
                author=Exitting(initialisation.book_author)
                theone = df[(df["Title"] == title) & (df["Author"] == author)]
                if theone.empty: 
                    print("This book doesn't exist.")
                    print("Try writing another name.")
                else:
                    thetwo = theone.iloc[0]
                    print(f"The Title of the Book: {thetwo['Title']}")
                    print(f"The Author of the Book: {thetwo['Author']}")
                    print(f"The Year of Release of the Book: {thetwo['Year']}")
                    print(f"The Genre of the Book: {thetwo['Genre']}")
            
            
            
def delete_book_byname(df):
    while True:
        
        thechoice=input("""
    1 -> If you want to Remove One Book 
    2 -> If you want ot remove  multiple books by something specific
    Enter your choice here : """)
        
        match thechoice:
            
            case '1':
                Exitting()
                title=initialisation.book_title()
                author=initialisation.book_author()
                
                if not df[(df['Title'] == title) & (df['Author'] == author)].empty:
                    df = df[~((df['Title'] == title) & (df['Author'] == author))] 
                    print(f"The book {title} by {author} has been removed.")
                    
                else:
                    print(f"The book {title} by {author} does not exist.")
                    
            case '2':       
                choice=input("""Choose Between the Availble Options 
                        1 -> Removing Books By Title. 
                        2 -> Removing Books By Author. 
                        3 -> Removing Books By Year.
                        4 -> Removing Books By Genre. 
                        Enter you Number here : """)
                
                match choice:
                    
                        case '1':
                            Exitting()
                            title=initialisation.book_title()
                            if df[(df['Title']==title) ].empty:
                                print("this books already dont exist Try another title")
                                return
                            else:
                                df=df[~(df['Title']==title)]
                                
                        case '2':
                            Exitting()
                            author=initialisation.book_author()
                            if df[(df['Author']==author) ].empty:
                                print("this books already dont exist Try another title")
                                return
                            else:
                                df=df[~(df['Author']==author)]
                                
                        case '3':
                            Exitting()
                            year=initialisation.book_year()
                            if df[(df['Year']==year) ].empty:
                                print("this books already dont exist Try another title")
                                return
                            else:
                                df=df[~(df['Year']==year)]
                                
                        case '4':
                            Exitting()
                            genre=initialisation.book_genre()
                            if df[(df['Genre']==genre) ].empty:
                                print("this books already dont exist Try another title")
                                return
                            else:
                                df=df[~(df['Genre']==genre)]
                            
                df.to_csv("thelibraryy.csv", index=False)
                
                
                
    
  
        
        
        
                    
    
            

    
    