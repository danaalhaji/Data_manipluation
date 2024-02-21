from abc import ABC , abstractmethod 




#define a class for a customers(account to have name email address and visa information)

class Customer:
    def __init__(self, name , email , address , visa_available:bool):
        self.name = name
        self.email = email
        self.address = address
        self.__visa_available = visa_available # make visa availablity private for security
        self.__visa_information = {"visa Numbe": "", "Visa Date": ""} #set the info to none until it is asigned by the user for security
    # visa available or not getter and setter 
    @property
    def visa(self):
        return self.__visa_available
    @visa.setter
    def visa_setter(self, available):
        self.__visa_available =  available
    @visa.getter
    def visa_getter(self):
        return self.__visa_available
    @visa.deleter
    def delete_visa_info(self):
        self.__visa_available = False
    @property
    def visa_info(self):
        return self.__visa_information
    @visa_info.setter
    #setting visa information to be able to use it in payment methods
    def visa_setting(self, visa_numb, visa_date):
        if self.visa_getter == True:
            self.__visa_information["visa Numbe"] =visa_numb
            self.__visa_info["Visa Date"] = visa_date
        #else:
        #    print("ERROR please check your registration info ")
    @visa_info.deleter
    def delete_my_visa(self):
        self.__visa_info = None
        self.__visa_available = False



#define book class where is has the title , the category , and realese data for the book  
class Book:
    #the publisher information
    publishers =[]
    def set_publisher(self,*publishers):
        for pob in publishers:
            self.publishers.append(pob)   
    #  book constructor  
    def __init__(self, title  , category , pdf_availabilty : bool , realease_date : int ,*args  ):
        self.title = title
        self.category = category
        self.authors = list(args) # every book may have many authors so i preffered to make them a list
        self.realease_date = realease_date
        self._pdf_availabilty = pdf_availabilty
    @property
    def pdf_av(self, availabilty):
        self._pdf_availabilty = availabilty

# Author class
class Author:
    def __init__(self,name ):
        self.name = name
        self.books = []
    def auth_books(self):
        return self.books
    # a method so we can add or change books for the author
    def add_book(self, books : Book):
        self.books.append(books)


''' every product must be book to have a quantity and price but not all books can be in the book shop so we have different class for a prodcuct'''
class BookAsProduct():
    def __init__(self,book, quantity, price):
        self.book = book
        self._quantity = quantity
        self.__price = price

# functions for the price to sett and get the price 

    @property
    def price(self):
        return self.__price
    #price setter
    @price.setter
    def set_price(self , price):
        self.__price = price

    @price.getter
    def get_price(self):
        return self.price
# functions for the price to set and get the quantity     
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def set_quantity(self, q):
        self._quantity = q
    @quantity.setter
    def change_quantity(self):
        if self._quantity > 0:
            self._quantity -= 1
        else:
            print(" This", super().title , "Is Sold Out")

'''payment method class preffered to be an interface because every book shop may have different payment method ''' 
class Payment_method(ABC):
    
    @abstractmethod
    def chash_on_delivery(self, address ):
        pass

    @abstractmethod
    def online_payment(self, visa_information):
        pass



class Book_Shop(Payment_method):
    def __init__(self , list_books , list_of_customers  ):
        self.__list_of_books = list(list_books)
        self.list_of_customers  = list(list_of_customers)

    @property
    def list_of_book(self):
        return self.__list_of_books
    #Setter for book list
    @list_of_book.setter
    def set_list(self, *args : BookAsProduct):
        for book in args:
            self.list_of_book.append(book)
    @list_of_book.getter
    def get_all_books(self):
        for b in self.__list_of_books:
            print("Name", b.book.title , "Price" , b.price , "Quantity Available:" ,
                b.quantity , "The book is availabe as PDF:" , b.book._pdf_availabilty)
    #set and get customers
    def set_customer(self , *customer: Customer):
        for c in customer:
            self.list_of_customers.append(c)
    def get_customer(self):
        for c in self.list_of_customers:
            print(c.name)

    def chash_on_delivery(self, address ):
        if address == True:
            return True
        else:
            return False
    def online_payment(self, visa_information):
        pass


class Cart(Book_Shop):
    def __init__(self, customer : Customer, *list_of_books: BookAsProduct  ):
        self.list_of_books = list(list_of_books)
        self.customer = customer
        self.list_of_wanted_books = []
        self.total = 0
    def add_book(self, book : BookAsProduct , quantity):
            self.list_of_wanted_books.append([book,quantity])
    def set_purchase(self):
        for p in self.list_of_wanted_books:
            self.total = self.total+(p[0].price * p[1])
        return self.total
    def make_purchase(self, pdf: bool , cash:bool , online:bool ):
        self.list_of_book[0]
        self.total = 0
        self.list_of_wanted_books = []
        self.customer = None
        if pdf == False:
            for p in self.list_of_books:
                p.book.change_quantity()
        if cash == True:
            return ("Thank you for purchasing from us")
        else:
            return("Thank you for purchasing from us !")

""" TESTINGGG !!!"""
customer1 = Customer("Dana" , "dana.alhaji95@gmail.com" , "Nablus" , True)
print(customer1)
book1 = Book("Python Tricks" , "Tech" , True , 2022 , "Mike")
book2 = Book("Python Tricks 2 " , "Tech" , True , 2022 , "Mike")
author1 = Author("Mike" )
author1.books.append(book1)
author1.books.append(book2)
print(author1.books)

book1_Product = BookAsProduct(book1,20,25)
book2_Product = BookAsProduct(book2,10,25)
my_book_shop = Book_Shop(list_books=[book1_Product,book2_Product], list_of_customers=[customer1])
my_book_shop.get_all_books
myCart = Cart(customer1 , book1_Product)
myCart.add_book(book1_Product,2)
myCart.add_book(book2_Product,5)
myCart.set_purchase()
print(myCart.set_purchase())
myCart.make_purchase(False , True , False)

