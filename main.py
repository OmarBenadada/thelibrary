import pandas as pd
from operation import lookingfor_books,adding_books

# Define a mock DataFrame to simulate the library
data = {
    "Title": ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice"],
    "Author": ["F. Scott Fitzgerald", "George Orwell", "Harper Lee", "Jane Austen"],
    "Year": [1925, 1949, 1960, 1813],
    "Genre": ["Fiction", "Dystopian", "Classic", "Romance"]
}
library_df = pd.DataFrame(data)

# Call the function for testing

adding_books(library_df)