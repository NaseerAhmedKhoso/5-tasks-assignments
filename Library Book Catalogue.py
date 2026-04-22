class Book:
    title=""
    author=""
    pages=""

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def summry(self):
        print("Book title :",self.title,"|","his author :",self.author,"|","it's pages :",self.pages)

b1=Book("Harry Potter and the Philosopher's Stone","J.K. Rowling",223)
b2=Book("The Alchemist","Paulo Coelho",197)
b3=Book("Think and Grow Rich ","Napoleon Hill",238)

b1.summry()
b2.summry()
b3.summry()