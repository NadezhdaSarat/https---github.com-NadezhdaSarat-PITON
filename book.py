class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def get_title(self):
        return self.title

    def get_autor(self):
        return self.autor

    def get_book_info(self):
        return f"Autor: {self.title}, Title: {self.autor}"