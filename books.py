import initialisation

class Books:
    def __init__(self, title=None, author=None, year=None, genre=None,content=None):
        self.title = title if title else initialisation.book_title()
        self.author = author if author else initialisation.book_author()
        self.year = year if year else initialisation.book_year()
        self.genre = genre if genre else initialisation.book_genre()
        self.content = content if content else initialisation.book_content()

        