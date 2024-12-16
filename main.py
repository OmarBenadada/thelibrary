import pandas as pd
from operation import lookingfor_books, adding_books, delete_book_byname

# Define columns for the DataFrame
columns = ['Title', 'Author', 'Year', 'Genre']

# Try to load existing data from CSV
try:
    library_df = pd.read_csv("thelibraryy.csv")
except FileNotFoundError:
    library_df = pd.DataFrame(columns=columns)  # If file doesn't exist, start with an empty DataFrame

# Call the function to delete a book by name
library_df = lookingfor_books(library_df)