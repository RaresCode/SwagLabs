import mysql.connector

class DatabaseConnector:
    
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="swaglads"
            )
            self.cursor = self.mydb.cursor(buffered=True)
        except mysql.connector.Error as err:
            print(f"Error during the connection: {err}")
        
    def get_products_data_names_asc(self):
        self.cursor.execute("SELECT * FROM PRODUCTS;")
        products = self.cursor.fetchall()
        # for product in self.products:
        #     print(product[1:])
        # print(self.products)
        return products

    def get_products_data_names_desc(self):
        self.cursor.execute("SELECT * FROM products ORDER BY product_name DESC;")
        products = self.cursor.fetchall()
        # for product in self.products:
        #     print(product[1:])
        # print(self.products)
        return products 
    
    def get_products_data_price_asc(self):
        self.cursor.execute("SELECT * FROM products ORDER BY product_price ASC;")
        products = self.cursor.fetchall()
        # for product in self.products:
        #     print(product[1:])
        # print(self.products)
        return products

    def get_products_data_price_desc(self):
        self.cursor.execute("SELECT * FROM products ORDER BY product_price DESC;")
        products = self.cursor.fetchall()
        # for product in self.products:
        #     print(product[1:])
        # print(self.products)
        return products 
    
    def get_order(self, first_name, last_name, zip_code):
        sql = "SELECT * FROM ORDERS WHERE FirstName = %s AND LastName = %s AND ZIP = %s"
        values = (first_name, last_name, zip_code)
        self.cursor.execute(sql, values)
        
        order = self.cursor.fetchall()
        # for product in self.products:
            # print(product[1:])
        # print(self.products)
        return order[0][1:]
        
    def add_order_details(self, first_name, last_name, zip_code):
        sql = "INSERT INTO ORDERS (FirstName, LastName, ZIP) VALUES (%s, %s, %s)"
        values = (first_name, last_name, zip_code)
        self.cursor.execute(sql, values)

        self.mydb.commit()
    
    def delete_order(self, first_name, last_name, zip_code):
        sql = "DELETE FROM ORDERS WHERE FirstName = %s AND LastName = %s AND ZIP = %s"
        values = (first_name, last_name, zip_code)
        self.cursor.execute(sql, values)
        
        self.mydb.commit()
    
if __name__ == "__main__":
    DatabaseConnector()
            
        