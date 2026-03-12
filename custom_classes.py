class Medialtem:
    def __init__(self, title, author, is_available): #sets the initial values of the objects
        self.title = title
        self.author = author
        self.is_available = True # attributes are written, in default form

    def __str__(self): #definin custom string representation for classes
        return f"{self.title} by {self.author}"
    
    def checkout(self): # name of the method
        if self.is_available:  # if the book is available, return successfull checkout
            self.is_available = False
            return str(self) + "Successfull checkout" 
        else: 
            return  str(self) + "Already out"  # return f"{self} Already out" is the best version.

    def return_item(self):
        self.is_available = True

class Book(Medialtem): #creating subclass

####super function used for calling the methods from the base class####
####so we can add subclasses, methods and attributes to the base class easily ####

    def __init__(self, title, author, is_available , page_count):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self): #adding the page number of the book 
        return f"{self.title} by {self.author} with {self.page_count} pages "
    
class DVD(Medialtem): #creating subclass

    def __init__(self, title, author, is_available, duration ):
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        result = super().checkout()  # call the base class checkout
        if "Successfull checkout" in result:
            print("Handle with care: Do not scratch the disc.")
        return result

class LibraryCollection:
    def __init__(self):
        self.container = []  # initialize empty list to store items

    def add_item(self, item):
        self.container.append(Book)
        self.container.append(DVD)   # add instances from Medialtem

    def list_items(self):
        for i, item in enumerate(self.container, 1):
            print(f"{i}. {item} - Available: {item.is_available}")








