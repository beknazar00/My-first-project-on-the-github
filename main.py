import psycopg2

conn = psycopg2.connect(database='lesson',
                        user='postgres',
                        host='localhost',
                        password='703',
                        port=5432)

cursor = conn.cursor()

select_all_books_query = '''
    select * from book;
'''
cursor.execute(select_all_books_query)
rows = cursor.fetchall()
for book in rows:
    print(book)