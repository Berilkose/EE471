#need to import the class from another script

from custom_classes import Book
'''
book = Medialtem("Korku", "Stefan Zweig", True)
movie = Medialtem("Inception", "Christopher Nolan", False) #two instances are created in the class Mediaterm

#simulating the checkout results
checkout_result = book.checkout()
print(checkout_result)
'''
'''
#check the status of the checkout
print("is book successfully checked? ")
print( book.is_available)
print("is movie successfully checked? ")
print(movie.is_available)
'''
# calling the subclasses for testing the code
'''
book_1 = Book("Korku", "Stefan Zweig", True, 175)
dvd_1 = DVD("Inception", "Christopher Nolan", False, 10)

print(book_1.checkout())
print(dvd_1.checkout())
'''
####Testing the Library####
# create library
#library = LibraryCollection()

# create items
book_1 = Book("Korku", "Stefan Zweig", True, 175)
#dvd_1 = DVD("Inception", "Christopher Nolan", True, 10)

# add items to library
#library.add_item(book_1)
#library.add_item(dvd_1)

# list all items
#library.list_items()
