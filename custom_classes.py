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
    
