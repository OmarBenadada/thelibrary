import pandas as pd
import books
import initialisation


def adding_books(df):
    print("if you want to quit the at any moment just type EXITP")
    while True:
        
        
        title = initialisation.book_title()
        if title.upper() == 'EXITP':
            print("Exiting...")
            break

        author = initialisation.book_author()
        if author.upper() == 'EXITP':
            print("Exiting...")
            break
        year = initialisation.book_year()
        if year.upper() == 'EXITP':
                print("Exiting...")
                break

        genre = initialisation.book_genre()
        if genre.upper() == 'EXITP':
                print("Exiting...")
                break
        
        if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
            print(f"this book {title} already Exist in the library ")
            continue
   
        else:
            book = books.Books(title=title, author=author, year=year, genre=genre)
            frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
            
            df=pd.concat([df,frame],axis=0,ignore_index=True)
            
            df.to_csv("TheFullLibrary.csv", index=False)
            
            print("book is added to the library")
            

def lookingfor_books(df):
    while True:
       
        bookss = books.Books() 
    
        theone = df[(df["Title"] == bookss.title) & (df["Author"] == bookss.author)]
        
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
    pass
    
    
            

    
    