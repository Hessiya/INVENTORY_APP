from datetime import date
import re
class Product:
    'python OOPs applied'
    def __init__(self,product_id=None,productname=None,unitprice=None,categoryid=None,manufacturedate=None,isactive="Y"):
        self.__product_id=product_id
        self.__productname=productname #validating productname
        self.__unitprice=unitprice
        self.__category_id=categoryid
        self.__manufacture_date=manufacturedate if manufacturedate else date.today()
        self.__is_active=isactive
    
    #------------------
    #getters and setters (using @property getters and setters)
    #------------------

    #getter and setter for parameters without @property anotation

    #getter setter for product id
    def get_product_id(self):
        return self.__product_id
    def set_product_id(self,product_id):
        self.__product_id=product_id
    #getter setter for product name with validation
    def get_productname(self):
        return self.__productname
    def set_product_name(self,productname):
        'validate product name before setting (2-30 alphabets/underscore)'
        pattern=re.compile(r"^[A-Za-z_]{2,30}$") #r=row text
        while True:
            if pattern.match(productname):
                self.__productname=productname
                break
            else:
                print("\t\t INvalid Product Name must have only alphabets, minimum character is 3...!!!!")
                productname=input("\t\t Enter Product name again: ")

    #getter setter for unit price
    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice=unitprice

    #getter setter for category id
    def get_categoryid(self):
        return self.__category_id
    def set_categoryid(self,categoryid):
        self.__category_id=categoryid
    
    #getter setter for manufacture date
    def get_manufacture_date(self):
        return self.__manufacture_date
    def set_manufacture_date(self,manufacture_date):
        if isinstance (manufacture_date,date):
            self.__manufacture_date=manufacture_date
        else:
            raise ValueError("manufacture date must be an date object")
    
    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active=is_active
    
    #override __str__
    def __str__(self):
        return f"productID: {self.__product_id:<10},productName: {self.__productname:<20} ,categoryID: {self.__category_id:<10}, UnitPrice: {self.__unitprice:<10}, ManufactureDate: {self.__manufacture_date:<15}, IsActive: {self.__is_active:<10}"
    
    
    
