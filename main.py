import psycopg2
from typing import Optional
conn = psycopg2.connect(database='lesson',
                        user='postgres',
                        host='localhost',
                        password='703',
                        port=5432)

cursor = conn.cursor()

# create_product_table = '''create table product(
#     id serial primary key,
#     name varchar(100) not null,
#     description text ,
#     price float check(price > 0),
#     image varchar(255) default 'https://amazon.com/image1'

# );
# '''

# cursor.execute(create_product_table)
# conn.commit()

class Product:
    def __init__(self,name:str,
                 description:Optional[str]=None,
                 price : Optional[float] = None,
                 image : Optional[str] = None
                 ):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
    
    
    def save(self):
        insert_into_query = '''
        insert into product(name,description,price,image)
        values (%s,%s,%s,%s);
        '''
        data = (self.name,self.description,self.price,self.image)
        cursor.execute(insert_into_query,data)
        conn.commit()


samsung  = Product('Samsung S 24 Ultra','The bestest product',24142.212,'image1')
samsung.save()


def func():
  print('123)
