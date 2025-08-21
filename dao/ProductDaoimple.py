from dao.AbstractProductDao import ProductDaoService
from db.db_connection import DBConnection
from models.product import Product
from typing import List

class ProductDaoImplementation(ProductDaoService):
    'implementation for abstract class'
    # SQL queries
    DISPLAY_ALL = "SELECT * FROM products"
    INSERT_PRODUCT = "INSERT INTO products(productname,unitprice,categoryid,manufacturedate,isactive) VALUES (%s,%s,%s,%s,%s)"
    FIND_BY_ID = "SELECT * FROM products WHERE product_id=%s"
    UPDATE_PRODUCT = "UPDATE products SET productname=%s, unitprice=%s WHERE product_id=%s"
    DISABLE_PRODUCT = "UPDATE products SET isactive = %s WHERE product_id = %s"
    APPLY_GST="CALL apply_gst_to_product(%s,%s)"


    def __init__(self):
        self.conn = DBConnection().get_connection()

    def insert_products(self, product: Product) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_PRODUCT, (
                product.get_productname(),
                product.get_unitprice(),
                product.get_categoryid(),
                product.get_manufacture_date(),
                product.get_is_active()
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:", e)
            return False
        finally:
            cursor.close()

    def display_all_products(self) -> List[Product]:
        products = []
        try:
            cursor = self.conn.cursor(dictionary=True) 
            cursor.execute(self.DISPLAY_ALL)
            rows = cursor.fetchall()
            for row in rows:
                products.append(Product(
                    product_id=row["product_id"],
                    productname=row["productname"],
                    unitprice=row["unitprice"],
                    categoryid=row["categoryid"],
                    manufacturedate=row["manufacturedate"],
                    isactive=row["isactive"]
                ))
        except Exception as e:
            print("Error fetching products:", e)
        finally:
            cursor.close()
        return products

    def find_by_product_id(self, product_id: int):
        product = None
        try:
            cursor = self.conn.cursor(dictionary=True) 
            cursor.execute(self.FIND_BY_ID, (product_id,))
            row = cursor.fetchone()
            if row:
                product = Product(
                    product_id=row["product_id"],
                    productname=row["productname"],
                    unitprice=row["unitprice"],
                    categoryid=row["categoryid"],
                    manufacturedate=row["manufacturedate"],
                    isactive=row["isactive"]
                )
        except Exception as e:
            print("Error finding product:", e)
        finally:
            cursor.close()
        return product

    def update_product(self, product: Product, product_id: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_PRODUCT, (
                product.get_productname(),
                product.get_unitprice(),
                product_id
            ))
            self.conn.commit()
            return cursor.rowcount == 1  
        except Exception as e:
            print("Error updating product:", e)
            return False
        finally:
            cursor.close()
    
    def disable_product(self, product_id:int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.DISABLE_PRODUCT, ("N", product_id))  # set inactive
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error in disabling the product...", e)
            return False
        finally:
            cursor.close()
    
    def apply_gst(self, product_id, gst_percent):
        cursor=None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.APPLY_GST,(product_id,gst_percent))
            self.conn.commit()
            return cursor.rowcount >=0 #since sp returns 0 if already appplied
        except Exception as e:
            print("Error applying GST:",e)
            return False
        finally:
            if cursor:
                cursor.close()